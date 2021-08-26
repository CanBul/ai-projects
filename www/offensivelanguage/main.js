function toggle() {
    
    const mobile = document.getElementById("mobile-nav");
    const mobileBtn1 = document.getElementById("mobile-btn1");
    const mobileBtn2 = document.getElementById("mobile-btn2");


    if (mobile.style.width === "") {
      mobile.style.width = "130px";
      document.body.style.height = "100vh";
      document.body.style.overflow = "hidden";

      mobileBtn1.style.transform = "scale(0)";
      mobileBtn2.style.transform = "scale(1)";
      document.getElementsByClassName("container1")[0].addEventListener('click', closeNav, true);

    } else {
      mobile.style.width = "";
      document.body.style.height = "100%";
      document.body.style.overflow = "";
      mobileBtn1.style.transform = "scale(1)";
      mobileBtn2.style.transform = "scale(0)";
    }
  }
const closeNav = function (e) {
const mobile = document.getElementById("mobile-nav");
const mobileBtn1 = document.getElementById("mobile-btn1");
const mobileBtn2 = document.getElementById("mobile-btn2");

if (document.getElementById("mobile-btn2").contains(e.target)) {
	document.getElementsByClassName("container1")[0].removeEventListener('click', closeNav, true);
} else {
	document.getElementsByClassName("container1")[0].removeEventListener('click', closeNav, true);
	mobile.style.width = "";
	document.body.style.height = "100%";
	document.body.style.overflow = "";
	mobileBtn1.style.transform = "scale(1)";
	mobileBtn2.style.transform = "scale(0)";
}
}



const reqServer = function () {
  document.getElementById("loading").style.display ="flex";
  const sendData =document.getElementById('data').value
  fetch("https://aiprojects.inzva.com/api/offensive", {
    method: "POST",
    headers: {
      Accept: "application/json, text/plain, */*",
      "Content-type": "application/json",
    },
    body: JSON.stringify(sendData),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById('result').style.display = 'block';
      document.getElementById('score').innerText = data.toFixed(2);
      document.getElementById("loading").style.display ="none";

      if (data < 0.5) {
        document.getElementById('resulttext').innerText= ' Your text is not Offensive';
        document.getElementById('resulttext').style.backgroundColor= 'rgba(92, 158, 245, 0.986)';

      } else {
        document.getElementById('resulttext').innerText= 'Your text is Offensive';
        document.getElementById('resulttext').style.backgroundColor= 'tomato';
      }
      

    }
    );

}

document.getElementById('btn').addEventListener('click', reqServer)