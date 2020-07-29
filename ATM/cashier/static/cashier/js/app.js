(() => {

    const userInput = document.querySelector("#money");
    const actionBtn = document.querySelector("#actionBtn");
    const error = document.querySelector("#error");

    const verifyMoneyInput = () => {
        isValid = false;
        if (userInput.value.length > 3 && parseInt(userInput.value) >= 1000) {
            isValid = true;
        }

        return isValid;
    };

    const events = () => {
        if (userInput) {
            userInput.addEventListener('keyup', () => {
                if (verifyMoneyInput()) {
                    actionBtn.disabled = false; 
                    error.style.display = 'none';
                }
                else {
                    actionBtn.disabled = true; 
                    error.style.display = 'block';
                }
            });
        }
    };

    const init = () => {
        if (actionBtn) {
            actionBtn.disabled = !verifyMoneyInput(); //Uses "!" because the atribute disabled is true if the input is invalid, false otherwise
            error.style.display = 'none';
        }
        events();
    };

    init();

})();