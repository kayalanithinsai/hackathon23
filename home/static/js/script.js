// Get the upload button element
const uploadButton = document.getElementById("upload-btn");

// Add event listener for the button click event
uploadButton.addEventListener("click", function () {
  // Add a CSS class to animate the button
  uploadButton.classList.add("animate-button");

  // Remove the CSS class after a delay
  setTimeout(function () {
    uploadButton.classList.remove("animate-button");
  }, 1000); // Adjust the delay duration (in milliseconds) as needed
});
