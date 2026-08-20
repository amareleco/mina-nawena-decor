console.log("Hello, world!");



// ========================================
// ELEMENTOS DO MODAL
// ========================================

const createClientModal =
    document.getElementById("createClientModal");

const createClientForm =
    document.getElementById("createClientForm");

const openCreateClientBtn =
    document.getElementById("openCreateClientBtn");

const closeCreateClientBtn =
    document.getElementById("closeCreateClientBtn");

const cancelCreateClientBtn =
    document.getElementById("cancelCreateClientBtn");


// ========================================
// ELEMENTOS adicionais do formulario
// ========================================

const clientCode =
    document.getElementById("client-Code");
    
const clientName =
    document.getElementById("client-name");

const clientPhone =
    document.getElementById("client-Phone");

const clientEmail =
    document.getElementById("client-email");

const clientAddress =
    document.getElementById("client-address");

const clientModalTitle =
    document.querySelector(".clt-modal-title");

const addClientBtn =
    document.querySelector(".clt-modal-title");
const dataCreated =
    document.getElementById("client-created-at");

// ========================================
// ABRIR MODAL
// ========================================

// openCreateProductBtn.addEventListener("click", () => {

//     createProductModal.classList.add("active");

// });


// ========================================
// FECHAR MODAL - BOTÃO X
// ========================================

closeCreateClientBtn.addEventListener("click", () => {

    createClientModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - BOTÃO CANCELAR
// ========================================

cancelCreateClientBtn.addEventListener("click", () => {

    createClientModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - CLICANDO FORA
// ========================================

createClientModal.addEventListener("click", (event) => {

    if (event.target === createClientModal) {

        createClientModal.classList.remove("active");

    }

});

// ========================================
// CRIAR PRODUTO
//========================================


createClientForm.addEventListener("submit", (event) => {

    event.preventDefault();

    const formData = new FormData(createClientForm);

    const client = {

        code: formData.get("client-Code"),

        name: formData.get("client-name"),

        telefone: formData.get("client-phone"),

        email: formData.get("client-email"),

        endereco: formData.get("client-address"),
        dataCriacao: new Date().toISOString().split("T")[0]


    };

});

let editingClientCode = null;

// ========================================
// Adicionar o cliente
// ========================================
openCreateClientBtn.addEventListener("click", () => {

    // Entrar no modo criação
    editingClientCode = null;

    // Limpar formulário
    createClientForm.reset();

    // Esconder código
    clientCode.hidden= true;

    //Esconder a data de criacao
    dataCreated.hidden= true;

    // Alterar título;

    // Alterar título
    clientModalTitle.textContent =
        "Adicionar cliente";

    // Alterar botão

    // Abrir modal
    createClientModal.classList.add("active");
});

// ========================================
// EDIÇÃO
// ========================================


const editClientButtons =
    document.querySelectorAll(".editClientButtons");

editClientButtons.forEach(button => {

    button.addEventListener("click", () => {

        // ========================================
        // ENTRAR NO MODO EDIÇÃO
        // ========================================

        editingClientCode =
            button.dataset.code;


        // ========================================
        // MOSTRAR CÓDIGO
        // ========================================


        clientCode.value =
            button.dataset.code;


        // Código não pode ser alterado

        clientCode.readOnly = true;


        // ========================================
        // PREENCHER CAMPOS
        // ========================================

        clientName.value =
            button.dataset.name;

        clientPhone.value =
            button.dataset.phone;

        clientEmail.value =
            button.dataset.email;

        clientAddress.value =
            button.dataset.address;

        // ========================================
        // ALTERAR TÍTULO
        // ========================================

        clientModalTitle.textContent =
            "Editar cliente";


        // ========================================
        // ALTERAR BOTÃO
        // ========================================

        // createCategoryForm.textContent =
        //     "Guardar alterações";


        // ========================================
        // ABRIR MODAL
        // ========================================

        createClientModal.classList.add("active");

    });

});


// CAMPO DE BUSCA 

// const clientSearch =
//     document.getElementById("clientSearch");

// const clientRows =
//     document.querySelectorAll(".client-row");


// clientSearch.addEventListener("input", () => {

//     const search =
//         clientSearch.value
//             .toLowerCase()
//             .trim();



//     clientRows.forEach(row => {

//         const text =
//             row.textContent.toLowerCase();


//         if (text.includes(search)) {

//             row.style.display = "";

//         } else {

//             row.style.display = "none";

//         }

//         // categorySearch .readOnly = true;

//     });

// });

