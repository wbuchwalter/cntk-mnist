# Ensure the training data is read and available for this tutorial
test_file = "data/MNIST/Test-28x28_cntk_text.txt"

if os.path.isfile(test_file):
    path = test_file
else:
    print("Please generate the data by completing CNTK 103 Part A")

feature_stream_name = 'features'
labels_stream_name = 'labels'

test_mb_source = text_format_minibatch_source(path, [
    StreamConfiguration(feature_stream_name, input_dim),
    StreamConfiguration(labels_stream_name, num_output_classes)])
features_si = mb_source[feature_stream_name]
labels_si = mb_source[labels_stream_name]

print("Test data from file {0} successfully read".format(path))

# Test data for trained model
test_minibatch_size = 512
num_samples = 10000
num_minibatches_to_test = num_samples / test_minibatch_size
test_result = 0.0
for i in range(0, int(num_minibatches_to_test)):
    mb = test_mb_source.next_minibatch(test_minibatch_size)

    # Specify the mapping of input variables in the model to actual
    # minibatch data to be tested with
    arguments = {input: mb[features_si],
                 label: mb[labels_si]}
    eval_error = trainer.test_minibatch(arguments)
    test_result = test_result + eval_error

# Average of evaluation errors of all test minibatches
print("Average test error: {0:.2f}%".format(test_result*100 / num_minibatches_to_test))