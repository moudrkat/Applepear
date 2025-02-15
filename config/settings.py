layer_info = {
    "conv2d": {
        "step": "Convolutional Layer 1",
        "description": "This is the first convolutional layer that scans the input sketch with small filters to find basic features. In my case, there are 32 filters, each applied on the sketch. Each filter produces a so-called 'feature map' - one of 36 tiny pictures you see below. The brighter parts show where I am detecting simple features like sharp lines in the sketch."
    },
    "max_pooling2d": {
        "step": "Pooling Layer 1",
        "description": "This is a pooling layer that reduces the size of the image by focusing on the most important features. The light areas highlight the most important parts of the sketch, simplifying the image while keeping the most relevant features."
    },
    "conv2d_1": {
        "step": "Convolutional Layer 2",
        "description": "This is the second convolutional layer that looks for more complex features in the sketch, building on the simple patterns identified by the first layer. Here 64 filters are applied. You'll see areas where I detect shapes that make up parts of the object in the sketch. For me, the sketch is nothing but areas of brighter and darker regions."
    },
    "max_pooling2d_1": {
        "step": "Pooling Layer 2",
        "description": "This is another pooling layer that further reduces the size of the image, allowing me to focus even more on the key features. The light areas represent the most important regions of the sketch that the pooling layer keeps, while simplifying the rest of the image."
    },
    "conv2d_2": {
        "step": "Convolutional Layer 3",
        "description": "This is a third convolutional layer, with 128 filters, that looks for even more advanced patterns based on what I have already found in previous layers. The activation image for this layer highlights the parts of the sketch where I detect high-level features. This is the final filtering of your picture which, in the next layer, I will convert to a different format in order to be able to make decisions."
    },
    "max_pooling2d_2": {
        "step": "Pooling Layer 3",
        "description": "This is another pooling layer that further reduces the size of the image, allowing me to focus even more on the key features. The light areas represent the most important regions of the sketch that the pooling layer keeps, while simplifying the rest of the image."
    },
    "flatten": {
        "step": "Flatten Layer",
        "description": "This layer flattens the 2D features into a simple 1D list of numbers - a format that I can use for decision-making in the next layers."
    },
    "dense": {
        "step": "Dense Layer 1",
        "description": "This is it. This is 'what makes an apple an apple or a pear a pear.' :) The fully connected (dense) layer links all the features together. Based on the patterns I have found in the previous layers, I start to combine the information to make predictions about what the sketch represents. The brighter areas show where I am focusing on specific features I am trained to recognize."
    },
    "dropout": {
        "step": "Dropout Layer",
        "description": "Reduce overfitting."
    },
    "dense_1": {
        "step": "Dense Layer 2",
        "description": "In the final dense layer, I make my decision (apple (left) / pear (right))."
    }
}
