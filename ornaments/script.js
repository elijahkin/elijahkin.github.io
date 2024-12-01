const renders = [
  {"src": "images/IMG_1890.JPG", "desc": "1995. Snidow Family Reunion"},
  {"src": "images/IMG_1866.JPG", "desc": "February 1996. Cape May, NJ"},
  {"src": "images/IMG_1858.JPG", "desc": "1998. Bubba"},
  {"src": "images/IMG_1922.JPG", "desc": "1998. White House Historical Association"},
  {"src": "images/IMG_1911.JPG", "desc": "1999. Bubba"},
  {"src": "images/IMG_1924.JPG", "desc": "1999. White House Historical Association"},
  {"src": "images/IMG_1907.JPG", "desc": "2000. Duck, NC"},
  {"src": "images/IMG_1940.JPG", "desc": "2000. White House Historical Association"},
  {"src": "images/IMG_1909.JPG", "desc": "2001. Duck, NC"},
  {"src": "images/IMG_1897.JPG", "desc": "2001. TODO"},
  {"src": "images/IMG_1938.JPG", "desc": "2001. White House Historical Association"},
  {"src": "images/IMG_1928.JPG", "desc": "2002. White House Historical Association"},
  {"src": "images/IMG_1949.JPG", "desc": "2003. White House Historical Association"},
  {"src": "images/IMG_1863.JPG", "desc": "December 2003. Charleston, SC"},
  {"src": "images/IMG_1910.JPG", "desc": "2004. Duck, NC"},
  {"src": "images/IMG_1944.JPG", "desc": "2004. White House Historical Association"},
  {"src": "images/IMG_1926.JPG", "desc": "2005. White House Historical Association"},
  {"src": "images/IMG_1884.JPG", "desc": "2006. White House Historical Association"},
  {"src": "images/IMG_1871.JPG", "desc": "August 2007. Snidow Family Reunion"},
  {"src": "images/IMG_1875.JPG", "desc": "2007. Richmond, VA. Virginia Pewtersmith"},
  {"src": "images/IMG_1877.JPG", "desc": "2007. Richmond, VA. Virginia Pewtersmith"},
  {"src": "images/IMG_1879.JPG", "desc": "2007. Richmond, VA. Virginia Pewtersmith"},
  {"src": "images/IMG_1881.JPG", "desc": "2007. Richmond, VA. Virginia Pewtersmith"},
  {"src": "images/IMG_1932.JPG", "desc": "2007. White House Historical Association"},
  {"src": "images/IMG_1920.JPG", "desc": "2008. White House Historical Association"},
  {"src": "images/IMG_1930.JPG", "desc": "2009. White House Historical Association"},
  {"src": "images/IMG_1854.JPG", "desc": "October 2010. Burlington, VT. Bob's 40th"},
  {"src": "images/IMG_1942.JPG", "desc": "2010. White House Historical Association"},
  {"src": "images/IMG_1914.JPG", "desc": "2011. White House Historical Association"},
  {"src": "images/IMG_1856.JPG", "desc": "2012. Camping with Scouts"},
  {"src": "images/IMG_1948.JPG", "desc": "2012. White House Historical Association"},
  {"src": "images/IMG_1946.JPG", "desc": "2013. White House Historical Association"},
  {"src": "images/IMG_1965.JPG", "desc": "2013. Swarovski Annual Edition"},
  {"src": "images/IMG_1916.JPG", "desc": "2014. White House Historical Association"},
  {"src": "images/IMG_1963.JPG", "desc": "2014. Swarovski Annual Edition"},
  {"src": "images/IMG_1918.JPG", "desc": "2015. White House Historical Association"},
  {"src": "images/IMG_1970.JPG", "desc": "2015. Swarovski Annual Edition"},
  {"src": "images/IMG_1934.JPG", "desc": "2016. White House Historical Association"},
  {"src": "images/IMG_1967.JPG", "desc": "2016. Swarovski Annual Edition"},
  {"src": "images/IMG_1968.JPG", "desc": "2017. Swarovski Annual Edition"},
  {"src": "images/IMG_1912.JPG", "desc": "2018. Scotland"},
  {"src": "images/IMG_1936.JPG", "desc": "2018. White House Historical Association"},
  {"src": "images/IMG_1957.JPG", "desc": "2018. Swarovski Annual Edition"},
  {"src": "images/IMG_1961.JPG", "desc": "2019. Swarovski Annual Edition"},
  {"src": "images/IMG_1905.JPG", "desc": "January 2020. Siesta Key, FL"},
  {"src": "images/IMG_1903.JPG", "desc": "2020. Macy"},
  {"src": "images/IMG_1959.JPG", "desc": "2020. Swarovski Annual Edition"},
  {"src": "images/IMG_1955.JPG", "desc": "2021. Swarovski Annual Edition"},
  {"src": "images/IMG_1951.JPG", "desc": "2022. Swarovski Annual Edition"},
  {"src": "images/IMG_1888.JPG", "desc": "April 2023. Cape May, NJ. Mami's High School Reunion"},
  {"src": "images/IMG_1953.JPG", "desc": "2023. Swarovski Annual Edition"},
  {"src": "images/IMG_1865.JPG", "desc": "2024. Savannah, GA"},
  {"src": "images/IMG_1861.JPG", "desc": "TODO. Tammie"},
  {"src": "images/IMG_1868.JPG", "desc": "TODO."},
  {"src": "images/IMG_1873.JPG", "desc": "TODO. Mami"},
  {"src": "images/IMG_1874.JPG", "desc": "TODO. Lucketts Ginkgo Leaf"},
  {"src": "images/IMG_1882.JPG", "desc": "TODO. Mami"},
  {"src": "images/IMG_1896.JPG", "desc": "TODO. Bird's Nest. Mami. Rose's Hair"},
  {"src": "images/IMG_1900.JPG", "desc": "TODO. 1997ish"},
  {"src": "images/IMG_1886.JPG", "desc": "TODO. 1997-2001ish"},
  {"src": "images/IMG_1893.JPG", "desc": "TODO. 2007ish. Eli"},
  {"src": "images/IMG_1895.JPG", "desc": "TODO. 2007ish. Baby Macy"},
  {"src": "images/IMG_1894.JPG", "desc": "TODO. 2007ish. Stella"},
  {"src": "images/IMG_1887.JPG", "desc": "TODO. St. Edward's"},
  {"src": "images/IMG_1869.JPG", "desc": "TODO. St. Edward's"}
];

var focused_idx;

function showImage(idx) {
  if (idx >= 0 && idx < renders.length) {
    focused_idx = idx;
    document.getElementById("image").src = renders[focused_idx].src;
    document.getElementById("description").textContent = renders[focused_idx].desc;
    document.getElementById("background").style.display = "block";

    MathJax.Hub.Queue(["Typeset", MathJax.Hub, document.getElementById("description")]);
    document.body.style.overflow = "hidden";
  }
}

function closeImage() {
  document.getElementById("background").style.display = "none";
  document.body.style.overflow = "auto";
}

document.addEventListener("keydown", (e) => {
  if (e.code === "Escape") closeImage()
  else if (e.code === "ArrowLeft") showImage(focused_idx - 1)
  else if (e.code === "ArrowRight") showImage(focused_idx + 1)
});

document.addEventListener("click", (e) => {
  if (e.target == document.getElementById("background")) {
    closeImage();
  }
});