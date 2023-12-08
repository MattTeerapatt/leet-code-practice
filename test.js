// Custom sorting function for alphanumeric strings using Bubble Sort
function alphanumericBubbleSort(arr) {
    var len = arr.length;
    for (var i = 0; i < len; i++) {
        for (var j = 0; j < len - i - 1; j++) {
            if (compareAlphanumeric(arr[j], arr[j + 1]) > 0) {
                // Swap elements if they are in the wrong order
                var temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Custom function to compare alphanumeric strings
function compareAlphanumeric(a, b) {
    var numA = extractNumber(a);
    var numB = extractNumber(b);

    if (!isNaN(numA) && !isNaN(numB)) {
        // Both are numbers, compare them directly
        return numA - numB;
    } else {
        // One or both are not numbers, compare them as strings
        return String(a).localeCompare(String(b));
    }
}

// Function to extract the numeric part from a string
function extractNumber(str) {
    var match = str.match(/\d+/);
    return match ? parseInt(match[0], 10) : NaN;
}

// Example array of alphanumeric strings
var inputArray = ["abc", "123", "def", "654", "zyx", "789", "ghi", "321"];

// Sort the array using the custom sorting function (Bubble Sort)
alphanumericBubbleSort(inputArray);

// Print the sorted array
console.log(inputArray);
