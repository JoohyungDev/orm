const result = document.querySelector(".cont-result");
const loading = document.querySelector(".result_loading");

function calculator() {
    // lablField, lablTime
    const fieldValue = document.querySelector("#lablField");
    let timeValue = document.querySelector("#lablTime");
    let timeValue_int = Number(timeValue.value);

    const fieldResult = document.querySelector(".field_result");
    const timeResult = document.querySelector(".time_result");

    if (fieldValue.value == "") {
        alert("입력되지 않았습니다.");
        fieldValue.focus();
        return false;
    } else if (timeValue.value == "") {
        alert("입력되지 않았습니다.");
        timeValue.focus();
        return false;
    } else if (timeValue_int > 24) {
        alert("잘못된 값입니다. 24이하의 값을 입력해 주세요");
        timeValue.focus();
        return false;
    }
    result.style.display = "flex";
    loading.style.display = "flex";

    setTimeout(function () {
        loading.style.display = none;
        result.style.display = "flex";
        fieldResult.innerText = parseInt(10000 / timeValue_int, 10);
    }, 1800);
}
