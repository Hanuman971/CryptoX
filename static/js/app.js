const refreshButtons = document.querySelectorAll(".ghost");

refreshButtons.forEach((button) => {
  button.addEventListener("click", (event) => {
    if (button.textContent.trim().toLowerCase() === "refresh") {
      event.preventDefault();
      button.textContent = "Updated";
      setTimeout(() => {
        button.textContent = "Refresh";
      }, 1200);
    }
  });
});
