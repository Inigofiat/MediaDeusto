if (!window.location.href.includes("index")) {
    const div = document.getElementById("FotoBlackFriday");
    div.innerHTML = "";
}

if (!window.location.href.includes("index")) {
  const div = document.getElementById("ofertas");
  if (div) {
      div.style.display = "none";
  }
}

if (!window.location.href.includes("index")) {
  const div = document.getElementById("productos")
  if (div) {
      div.style.display = "none";
  }
}


/*function scrollToLeft() {
  const container = document.getElementById('modelos-container');
  const modeloItem = document.querySelector('.modelo-item');
  
  const itemWidth = modeloItem.offsetWidth + 15; 
  
  if (container.scrollLeft > 0) {
    container.scrollLeft -= itemWidth;
  }
}

function scrollToRight() {
  const container = document.getElementById('modelos-container');
  const modeloItem = document.querySelector('.modelo-item');
  
  const itemWidth = modeloItem.offsetWidth + 15;
  

  if (container.scrollLeft < container.scrollWidth - container.clientWidth) {
    container.scrollLeft += itemWidth;
  }
}*/

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('modelos-container');
  container.scrollLeft = 0; // Garantizamos que comience en 0
});

