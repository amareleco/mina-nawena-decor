console.log("Hello, world!")

const usersTableBody =
    document.getElementById("users-table-body");

let usersData = [];

const roleLabels = {
    admin: "Administrador",
    manager: "Gestor",
    employee: "Empregado"
};

async function loadUsers() {

    try {

        const response = await apiFetch(
            `${API_URL}/users/`
        );

        if (!response.ok) {
            throw new Error(
                `Erro HTTP: ${response.status}`
            );
        }

        const users = await response.json();

        usersData = users;

        console.log("Usuários:", users);

        renderUsers(users);

    } catch (error) {

        console.error(
            "Erro ao carregar usuários:",
            error
        );

    }
}


function renderUsers(users) {

    usersTableBody.innerHTML = "";

    users.forEach(user => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${user.code}</td>

            <td>${user.name}</td>

            <td>${user.email}</td>

            <td> ${roleLabels[user.role] ?? user.role}</td>

            <td>
                ${user.is_active ? "Ativo" : "Inativo"}
            </td>

            <td>${user.created_at ?? ""}</td>

            <td class="actions text-center">

                <button
                    class="btn-action edit edit-user-btn"
                    data-code="${user.code}"
                    title="Editar usuário"
                >
                    <i class="fas fa-pen"></i>
                </button>

                <button
                    class="btn-action delete delete-user-btn"
                    data-code="${user.code}"
                    title="Eliminar usuário"
                >
                    <i class="fas fa-trash-alt"></i>
                </button>

            </td>
        `;

        usersTableBody.appendChild(row);
    });
}

document.addEventListener(
    "DOMContentLoaded",
    () => {
        loadUsers();
    }
);

const createUserModal =
    document.getElementById("createUserModal");

const createUserForm =
    document.getElementById("createUserForm");

const addUserBtn =
    document.getElementById("addUserBtn");

const closeCreateUserBtn =
    document.getElementById("closeCreateUserBtn");

const cancelCreateUserBtn =
    document.getElementById("cancelCreateUserBtn");

const userNameInput =
    document.getElementById("userName");

const userEmailInput =
    document.getElementById("userEmail");

const userPasswordInput =
    document.getElementById("userPassword");

const userRoleInput =
    document.getElementById("userRole");

const userActiveInput =
    document.getElementById("userActive");

const userCodeInput =
    document.getElementById("userCode");

const userModalTitle =
    document.querySelector(".userModalTitle")



let editingUserCode = null;

addUserBtn.addEventListener("click", () => {

    createUserForm.reset();

    userCodeInput.value = "";

    userCodeInput.hidden = true;

    userCodeInput.required = false;

    userModalTitle.textContent =
            "Cadastro do Utilizador";

    createUserModal.classList.add("active");


});

closeCreateUserBtn.addEventListener("click", () => {

    createUserModal.classList.remove("active");

});

cancelCreateUserBtn.addEventListener("click", () => {

    createUserModal.classList.remove("active");

});



//POST

createUserForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        const userData = {

            name: userNameInput.value.trim(),

            email: userEmailInput.value.trim(),

            password: userPasswordInput.value,

            role: userRoleInput.value,

            is_active: userActiveInput.value

        };

        console.log(
            "DADOS DO USUÁRIO:",
            userData
        );

        let url;
        let method;

        if (editingUserCode) {

            url =
                `${API_URL}/users/${editingUserCode}`;

            method = "PUT";

        } else {

                url =
                    `${API_URL}/users/`;

                method = "POST";
            }

        try {

            const response = await apiFetch(
                    url,
                    {
                        method: method,

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify(userData)
                    }
                );

            const data =
                await response.json();

            console.log(
                "STATUS:",
                response.status
            );

            console.log(
                "RESPOSTA:",
                data
            );

            if (!response.ok) {

                throw new Error(
                    JSON.stringify(data)
                );

            }

            // Atualizar tabela
            await loadUsers();

            // Limpar formulário

             editingUserCode = null;

            createUserForm.reset();

            userPasswordInput.required = true;

            // Fechar modal
            createUserModal.classList.remove(
                "active"
            );

        } catch (error) {

            console.error(
                "Erro ao criar usuário:",
                error
            );

        }

    }
);

// Put

const addUserEditBtn =
document.querySelector(".addUserEditBtn")

usersTableBody.addEventListener(
    "click",
    async (event) => {

        const editButton =
            event.target.closest(
                ".edit-user-btn"
            );

        if (!editButton) {
            return;
        }

        const code =
            editButton.dataset.code;

        const user =
            usersData.find(
                item => item.code === code
            );

        if (!user) {
            return;
        }

        console.log(
            "USUÁRIO PARA EDITAR:",
            user
        );

        editingUserCode = user.code;

        userNameInput.value =
            user.name;

        userEmailInput.value =
            user.email;

        userRoleInput.value =
            user.role;

        userActiveInput.value =
            user.is_active;
        
        userCodeInput.hidden = false;

        userCodeInput.value =
            user.code;

        
        userModalTitle.textContent =
            "Atualizar os dados do Utilizador";

         addUserEditBtn.textContent =
            "Guardar alteracoes";


        // Não colocar senha existente
        userPasswordInput.value = "";

        // Se a senha não for obrigatória na edição
        userPasswordInput.required = false;

        createUserModal.classList.add(
            "active"
        );

    }
);


usersTableBody.addEventListener(
    "click",
    async (event) => {

        const deleteButton =
            event.target.closest(
                ".delete-user-btn"
            );

        if (!deleteButton) {
            return;
        }

        const code =
            deleteButton.dataset.code;

        const confirmed =
            confirm(
                `Deseja eliminar o usuário ${code}?`
            );

        if (!confirmed) {
            return;
        }

        try {

            const response =
                await apiFetch(
                    `${API_URL}/users/${code}`,
                    {
                        method: "DELETE"
                    }
                );

            console.log(
                        "DELETE STATUS:",
                        response.status
                    );

                    if (!response.ok) {

                        const errorData = await response.text();

                        throw new Error(
                            errorData || `Erro HTTP: ${response.status}`
                        );
                    }

            await loadUsers();

        } catch (error) {

            console.error(
                "Erro ao eliminar usuário:",
                error
            );

        }

    }
);

const userSearchInput =
    document.getElementById("userSearchInput");


userSearchInput.addEventListener(
    "input",
    () => {

        const search =
            userSearchInput.value
                .trim()
                .toLowerCase();

        if (!search) {

            renderUsers(usersData);

            return;
        }

        const filteredUsers =
            usersData.filter(user => {

                return (
                    user.code
                        ?.toLowerCase()
                        .includes(search)

                    ||

                    user.name
                        ?.toLowerCase()
                        .includes(search)

                    ||

                    user.email
                        ?.toLowerCase()
                        .includes(search)
                );

            });

        renderUsers(filteredUsers);

    }
);