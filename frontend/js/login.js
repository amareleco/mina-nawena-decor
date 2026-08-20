const loginForm = document.getElementById("login-form");
const loginError = document.getElementById("login-error");

loginForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    loginError.textContent = "";

    const email =
        document.getElementById("email").value.trim();

    const password =
        document.getElementById("password").value;

    const formData = new URLSearchParams();

    formData.append("username", email);
    formData.append("password", password);

    try {

        const response = await fetch(
            `${API_URL}/api/v1/login/access-token`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/x-www-form-urlencoded"
                },

                body: formData
            }
        );

        const data = await response.json();

        if (!response.ok) {

            throw new Error(
                data.detail ||
                "E-mail ou senha inválidos."
            );

        }

        localStorage.setItem(
            "access_token",
            data.access_token
        );

        if (data.token_type) {

            localStorage.setItem(
                "token_type",
                data.token_type
            );

        }

        window.location.href = "../index.html";

    } catch (error) {

        console.error(
            "Erro no login:",
            error
        );

        loginError.textContent =
            error.message;

    }

});