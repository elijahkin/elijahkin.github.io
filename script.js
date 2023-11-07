var focused_idx;

const images = ["images/1.png", "images/2.png", "images/3.png", "images/4.png", "images/5.png", "images/6.png", "images/7.png", "images/8.png", "images/9.png", "images/10.png", "images/11.png", "images/12.png", "images/13.png", "images/14.png", "images/15.png", "images/16.png"];
const names = ["Function 1", "Function 2", "Function 3", "Function 4", "Function 5", "Function 6", "Function 7", "Function 8", "Function 9", "Function 10", "Function 11", "Function 12", "Function 13", "Function 14", "Function 15", "Function 16"];
const descriptions = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "Congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque.", "Est lorem ipsum dolor sit amet consectetur adipiscing.", "Morbi tristique senectus et netus et malesuada.", "Mi eget mauris pharetra et.", "Blandit turpis cursus in hac habitasse platea.", "Bibendum est ultricies integer quis auctor elit sed vulputate.", "Morbi enim nunc faucibus a pellentesque sit amet.", "Tincidunt arcu non sodales neque sodales.", "Dictum non consectetur a erat nam.", "Vel turpis nunc eget lorem dolor.", "Suspendisse potenti nullam ac tortor vitae purus faucibus ornare.", "Sollicitudin ac orci phasellus egestas tellus rutrum.", "Mauris pharetra et ultrices neque ornare aenean.", "Fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus.", "Donec massa sapien faucibus et molestie ac."];

function showImage(idx) {
  if (idx >= 0 && idx < images.length) {
    focused_idx = idx;
    document.getElementById("focused").src = images[focused_idx];
    document.getElementById("name").innerHTML = names[focused_idx];
    document.getElementById("description").innerHTML = descriptions[focused_idx];
    document.getElementById("filter").style.display = "block";
  }
}

function closeImage() {
  document.getElementById("filter").style.display = "none";
}

document.addEventListener("keydown", (e) => {
  if (e.code === "Escape") closeImage()
  else if (e.code === "ArrowLeft") showImage(focused_idx - 1)
  else if (e.code === "ArrowRight") showImage(focused_idx + 1)
});

document.addEventListener('click', (e) => {
  if (e.target == document.getElementById('filter')) {
    closeImage();
  }
});