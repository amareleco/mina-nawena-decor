console.log("Hello, world!");



// ========================================
// ELEMENTOS DO MODAL
// ========================================

const createSupplierModal =
    document.getElementById("createSupplierModal");

const createSupplierForm =
    document.getElementById("createSupplierForm");

const openCreateSupplierBtn =
    document.getElementById("openCreateSupplierBtn");

const closeCreateSupplierBtn =
    document.getElementById("closeCreateSupplierBtn");

const cancelCreateSupplierBtn =
    document.getElementById("cancelCreateSupplierBtn");


// ========================================
// ELEMENTOS adicionais do formulario
// ========================================

const supplierCode =
    document.getElementById("supplier-code");
    
const supplierName =
    document.getElementById("supplier-name");

const supplierPhone =
    document.getElementById("supplier-contact");

const supplierEmail =
    document.getElementById("supplier-email");

const supplierAddress =
    document.getElementById("supplier-address");

const supplierModalTitle =
    document.querySelector(".sup-modal-title");

const addSupplierBtn =
    document.querySelector(".sup-modal-title");
const dataCreated =
    document.getElementById("supplier-created-at");

// ========================================
// ABRIR MODAL
// ========================================

// openCreateProductBtn.addEventListener("click", () => {

//     createProductModal.classList.add("active");

// });


// ========================================
// FECHAR MODAL - BOTÃO X
// ========================================

closeCreateSupplierBtn.addEventListener("click", () => {

    createSupplierModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - BOTÃO CANCELAR
// ========================================

cancelCreateSupplierBtn.addEventListener("click", () => {

    createSupplierModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - CLICANDO FORA
// ========================================

createSupplierModal.addEventListener("click", (event) => {

    if (event.target === createSupplierModal) {

        createSupplierModal.classList.remove("active");

    }

});

// ========================================
// CRIAR PRODUTO
//========================================


createSupplierForm.addEventListener("submit", (event) => {

    event.preventDefault();

    const formData = new FormData(createSupplierForm);

    const supplier = {

        code: formData.get("supplier-Code"),

        name: formData.get("supplier-name"),

        telefone: formData.get("supplier-contact"),

        email: formData.get("supplier-email"),

        address: formData.get("supplier-address"),
        dataCriacao: new Date().toISOString().split("T")[0]


    };

});

let editingSupplierCode = null;

// ========================================
// Adicionar o cliente
// ========================================
openCreateSupplierBtn.addEventListener("click", () => {
    
    // Entrar no modo criação
    editingSupplierCode = null;

    // Limpar formulário
    createSupplierForm.reset();

    // Esconder código
    supplierCode.hidden= true;

    //Esconder a data de criacao
    dataCreated.hidden= true;

    // Alterar título;

    // Alterar título
    supplierModalTitle.textContent =
        "Adicionar fornecedor";

    // Alterar botão

    // Abrir modal
    createSupplierModal.classList.add("active");
});

// ========================================
// EDIÇÃO
// ========================================


const editSupplierButtons =
    document.querySelectorAll(".editSupplierButtons");

editSupplierButtons.forEach(button => {

    button.addEventListener("click", () => {

        // ========================================
        // ENTRAR NO MODO EDIÇÃO
        // ========================================

        editingSupplierCode =
            button.dataset.code;


        // ========================================
        // MOSTRAR CÓDIGO
        // ========================================


        supplierCode.value =
            button.dataset.code;


        // Código não pode ser alterado

        supplierCode.readOnly = true;


        // ========================================
        // PREENCHER CAMPOS
        // ========================================

        supplierName.value =
            button.dataset.name;

        supplierPhone.value =
            button.dataset.telefone;

        supplierEmail.value =
            button.dataset.email;

        supplierAddress.value =
            button.dataset.address;

        // ========================================
        // ALTERAR TÍTULO
        // ========================================

        supplierModalTitle.textContent =
            "Editar fornecedor";


        // ========================================
        // ALTERAR BOTÃO
        // ========================================

        // createCategoryForm.textContent =
        //     "Guardar alterações";


        // ========================================
        // ABRIR MODAL
        // ========================================

        createSupplierModal.classList.add("active");

    });

});


// CAMPO DE BUSCA 

// const supplierSearch =
//     document.getElementById("supplierSearch");

// const supplierRows =
//     document.querySelectorAll(".supplier-row");


// supplierSearch.addEventListener("input", () => {

//     const search =
//         supplierSearch.value
//             .toLowerCase()
//             .trim();



//     supplierRows .forEach(row => {

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

