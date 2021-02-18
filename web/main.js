var body, num, array, width, context, logo, myElements, analyser, src, height;
body = document.querySelector('body');

num = 28;

array = new Uint8Array(num*2);

width = 10;

window.onclick = function(){
    if(context) return;

    for(var i = 0; i < num; i++) {
        logo = document.createElement('div');
        logo.className = 'logo';
        logo.style.background =  "#de6161";  /* fallback for old browsers */
        logo.style.background = "-webkit-linear-gradient(to right, #2657eb, #de6161)";  /* Chrome 10-25, Safari 5.1-6 */
        logo.style.background = "linear-gradient(to right, #2657eb, #de6161)"; /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        ;
        logo.style.minWidth = width + 'px';
        body.appendChild(logo);
    }
    myElements = document.getElementsByClassName('logo');
    context = new AudioContext();
    analyser = context.createAnalyser();

    navigator.mediaDevices.getUserMedia({
        audio: true
    }).then(stream => {
        src = context.createMediaStreamSource(stream);
        src.connect(analyser);
        loop();
    }).catch(error => {
        alert(error + '\r\n\ Отклонено. Приложение будет обновлено!');
        location.reload();
    });
}

function loop() {
    window.requestAnimationFrame(loop);
    analyser.getByteFrequencyData(array);
    for(var i = 0; i < num; i++) {
        height = array[i+num];
        myElements[i].style.minHeight =height + 'px';
        myElements[i].style.opacity = 0.010 * height;
    }
}
