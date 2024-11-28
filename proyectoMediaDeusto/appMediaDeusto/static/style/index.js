if (!window.location.href.includes("index")) {
    const div = document.getElementById("FotoBlackFriday");
    div.innerHTML = "";
}

document.addEventListener("DOMContentLoaded", function () {
    const modelosContainer = document.getElementById("modelos-container");
  
    // Evento para mostrar un mensaje dinámico al hacer clic en un modelo
    modelosContainer.addEventListener("click", function (e) {
      if (e.target.classList.contains("modelo-img")) {
        // Obtener el modelo clicado
        const modeloItem = e.target.closest(".modelo-item");
        const modeloPrecio = modeloItem.querySelector(".modelo-precio").innerText;
  
        // Crear un mensaje flotante
        const mensaje = document.createElement("div");
        mensaje.innerText = `¡Has seleccionado un modelo de ${modeloPrecio}!`;
        mensaje.style.position = "fixed";
        mensaje.style.top = "20px";
        mensaje.style.left = "50%";
        mensaje.style.transform = "translateX(-50%)";
        mensaje.style.backgroundColor = "#ff0000";
        mensaje.style.color = "#fff";
        mensaje.style.padding = "10px 20px";
        mensaje.style.borderRadius = "5px";
        mensaje.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
        mensaje.style.zIndex = "1000";
        document.body.appendChild(mensaje);
  
        // Eliminar el mensaje después de 2 segundos
        setTimeout(() => {
          mensaje.remove();
        }, 2000);
      }
    });
  
    // Evento para cambiar el estilo al pasar el ratón sobre una imagen
    modelosContainer.addEventListener("mouseover", function (e) {
      if (e.target.classList.contains("modelo-img")) {
        e.target.style.border = "3px solid #ff0000"; // Añadir borde rojo
        e.target.style.cursor = "pointer"; // Cambiar cursor
      }
    });
  
    // Evento para restaurar el estilo original al salir el ratón
    modelosContainer.addEventListener("mouseout", function (e) {
      if (e.target.classList.contains("modelo-img")) {
        e.target.style.border = "2px solid #ddd"; // Restaurar borde original
      }
    });
  });