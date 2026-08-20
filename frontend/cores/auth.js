
function requireAuth() {
    const token = localStorage.getItem("access_token");

    if (!token) {
        window.location.href = "login.html";
    }
}



function getToken() {

    return localStorage.getItem("access_token");

}


async function apiFetch(url, options = {}) {

    const token = getToken();

    const headers = {
        ...(options.headers || {})
    };

    if (token) {
        headers["Authorization"] =
            `Bearer ${token}`;
    }

    const response = await fetch(url, {
        ...options,
        headers
    });

    // Token inválido ou expirado
    if (response.status === 401) {

        alert(
            "Sua sessão expirou ou não é válida. Faça login novamente."
        );

        localStorage.removeItem("access_token");
        localStorage.removeItem("token_type");

        window.location.href = "login.html";

        return response;
    }

    // Usuário autenticado, mas sem permissão
    if (response.status === 403) {

        let message =
            "Você não tem permissão para realizar esta operação.";

        try {

            const data =
                await response.clone().json();

            if (data.detail) {
                message = data.detail;
            }

        } catch (error) {

            console.warn(
                "Não foi possível ler a mensagem de autorização."
            );

        }

        alert(`Ação negada\n\n${message}`);

        return response;
    }

    return response;
}


function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("access_token");
    localStorage.removeItem("token_type");

    sessionStorage.clear();

    window.location.href = "login.html";
}