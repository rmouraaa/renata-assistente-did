const chatbox = document.querySelector(".chatbox");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");
const videoElement = document.querySelector(".video-container video");

let userName = new URLSearchParams(window.location.search).get("name");
let questionIndex = 0;
let userAnswers = {};

const questions = [
  `Bom dia, ${userName}. Qual a grande novidade para a equipe Renova temos hoje?`,
  `Excelente. É uma novidade incrível, agora me conta ${userName}, o que gostaria de destacar?`,
  `Ótimo, agora só mais uma pergunta. E por fim, última, prometo ${userName}, você quer vídeo e e-mail marketing ou somente um dos itens?`,
];

const videos = [
  "/static/video/step01.mp4",
  "/static/video/step02.mp4",
  "/static/video/step03.mp4",
  "/static/video/step04.mp4",
];

function updateVideoSource(index) {
  if (videos[index]) {
    videoElement.setAttribute("src", videos[index]);
    videoElement.load();
    videoElement.play();
  }
}

function downloadVideo(videoPath) {
  const link = document.createElement("a");
  link.href = videoPath;
  link.download = "";
  link.click();
}

function addMessage(content, isUser = false, userAnswer = null) {
  const msgDiv = document.createElement("div");
  msgDiv.innerText = content;
  msgDiv.className = isUser ? "user-message" : "system-message";
  chatbox.appendChild(msgDiv);
  chatbox.scrollTop = chatbox.scrollHeight;

  if (
    content ==
    "Excelente, agora é só aguardar alguns minutos, vou gerar o seu comunicado incrível."
  ) {
    $.ajax({
      url: "/generate_video",
      type: "POST",
      data: JSON.stringify(userAnswers),
      contentType: "application/json",
      success: function (response) {
        const videoPath = response.video_path;
        addMessage(`O seu vídeo está pronto ${userName}. Agora, é só baixar.`);
        downloadVideo(videoPath);
      },
      error: function (error) {
        console.log(error);
        alert(
          "Ocorreu um erro ao gerar o vídeo. Por favor, tente novamente mais tarde."
        );
      },
    });
  }
}

function sendAnswer() {
  const answer = userInput.value.trim();
  userAnswers[`resposta${questionIndex + 1}`] = answer;
  if (answer) {
    addMessage(answer, true, answer);
    userInput.value = "";
    questionIndex++;
    updateVideoSource(questionIndex);
    if (questionIndex < questions.length) {
      setTimeout(() => addMessage(questions[questionIndex]), 1000);
    } else {
      setTimeout(
        () =>
          addMessage(
            "Excelente, agora é só aguardar alguns minutos, vou gerar o seu comunicado incrível."
          ),
        1000
      );
      userInput.disabled = true;
      sendBtn.disabled = true;
    }
  }
}

sendBtn.addEventListener("click", sendAnswer);
userInput.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    sendAnswer();
  }
});

addMessage(questions[0]);
updateVideoSource(0);
