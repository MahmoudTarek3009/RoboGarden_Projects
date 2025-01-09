// Function to calculate the GPA
function calculateGPA(arr) {
    let gradeToNumeric = {
        "A": 100,
        "B": 80,
        "C": 70,
        "D": 60,
        "F": 50
    };

    let total = 0;

    // Loop through the grades array, convert each grade to numeric, and sum them up
    for (let i = 0; i < arr.length; i++) {
        if (gradeToNumeric[arr[i]] !== undefined) {
            total += gradeToNumeric[arr[i]];
        } else {
            console.log("Invalid grade found: " + arr[i]);
        }
    }

    // Calculate the average GPA
    let averageNumeric = total / arr.length;

    // Convert the numeric GPA back to an alphabetic grade
    let averageGrade = "";

    if (averageNumeric >= 90) {
        averageGrade = "A";
    } else if (averageNumeric >= 80) {
        averageGrade = "B";
    } else if (averageNumeric >= 70) {
        averageGrade = "C";
    } else if (averageNumeric >= 60) {
        averageGrade = "D";
    } else {
        averageGrade = "F";
    }

    // Display the result
    document.write("Your GPA is: " + averageGrade);
    // Optionally, you can also log it to the console
    console.log("Your GPA is: " + averageGrade);
}

// Call the function with an array of grades (this is an example)
calculateGPA(["A", "B", "C"]);
