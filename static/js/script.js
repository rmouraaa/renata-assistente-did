window.onload = function () {
  let video = document.querySelector("video");
  let inputField = document.querySelector(".chat input");
  let button = document.querySelector(".chat button");

  inputField.addEventListener("focus", function () {
    if (video.paused) {
      video.play();
    }
  });

  button.addEventListener("click", function () {
    let userName = inputField.value;
    location.href = "/chat?name=" + encodeURIComponent(userName);
  });
};
