const renders = [
  {"name": "Sirby", "src": "images/1.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Ooze", "src": "images/2.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Pollock", "src": "images/3.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Needle", "src": "images/4.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Cannon", "src": "images/5.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Misiurewicz", "src": "images/6.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Acid Pitchfork", "src": "images/7.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Triangle Dragon", "src": "images/8.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Roots of Unity", "src": "images/9.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Strawberry Banana", "src": "images/10.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Whirlpool", "src": "images/11.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Branch Cut", "src": "images/12.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Blossom", "src": "images/13.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Long Eli", "src": "images/14.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Iridescence", "src": "images/15.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Burning Ship", "src": "images/16.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Sleepy Cleo", "src": "images/17.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Under Construction", "src": "images/18.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Carpet", "src": "images/19.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Pastel Oology", "src": "images/20.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Essential Singularity", "src": "images/21.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Ex Nihilo", "src": "images/22.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Jake & Maggie", "src": "images/23.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Grace", "src": "images/24.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Iterated Map 1", "src": "images/25.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Iterated Map 2", "src": "images/26.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Iterated Map 3", "src": "images/27.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Kaleidoscope", "src": "images/28.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Lacunary", "src": "images/29.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "CMYK", "src": "images/30.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Crevice", "src": "images/31.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
  {"name": "Tron", "src": "images/32.png", "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}
];

var focused_idx;

function showImage(idx) {
  if (idx >= 0 && idx < renders.length) {
    focused_idx = idx;
    document.getElementById("focused").src = renders[focused_idx].src;
    document.getElementById("name").innerHTML = renders[focused_idx].name;
    document.getElementById("description").innerHTML = renders[focused_idx].desc;
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

document.addEventListener("click", (e) => {
  if (e.target == document.getElementById("filter")) {
    closeImage();
  }
});