function showImage(imageSrc) {
  document.getElementById("focused").src = imageSrc;
  document.getElementById("filter").style.display = "block";
}

function closeImage() {
  document.getElementById("filter").style.display = "none";
}

document.addEventListener("keyup", (e) => {
  if (e.code === "Escape") closeImage()
  else if (e.code === "ArrowLeft") closeImage()
  else if (e.code === "ArrowRight") closeImage()
});

document.addEventListener('click', (e) => {
  if (e.target == document.getElementById('filter')) {
    closeImage();
  }
});