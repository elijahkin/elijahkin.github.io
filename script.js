var focused_idx;

function showImage(idx) {
  if (idx > 0 && idx <= 16) {
    focused_idx = idx;
    document.getElementById("focused").src = "images/" + focused_idx + ".png";
    document.getElementById("filter").style.display = "block";
  }
}

function closeImage() {
  document.getElementById("filter").style.display = "none";
}

document.addEventListener("keyup", (e) => {
  if (e.code === "Escape") closeImage()
  else if (e.code === "ArrowLeft") showImage(focused_idx - 1)
  else if (e.code === "ArrowRight") showImage(focused_idx + 1)
});

document.addEventListener('click', (e) => {
  if (e.target == document.getElementById('filter')) {
    closeImage();
  }
});