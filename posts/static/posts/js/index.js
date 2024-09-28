export const nameVal = document.getElementById('name');
const enterBtn = document.getElementById('enterBtn');
const header = document.getElementById('header');
const goToDiary = document.getElementById('goToDiary')

enterBtn.addEventListener('click', () => {
    if (nameVal.value != ""){
        header.innerText = "Hello, " + nameVal.value
        goToDiary.classList.toggle('hidden');
        nameVal.classList.toggle('hidden');
        enterBtn.classList.toggle('hidden');
    }
})


