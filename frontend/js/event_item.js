console.log("Hello, world!");



// ========================================
// ELEMENTOS DO MODAL
// ========================================

const createEventItemModal =
    document.getElementById("createEventItemModal");

const createEventItemForm =
    document.getElementById("createEventItemForm");

const openCreateEventItemBtn =
    document.getElementById("openCreateEventItemBtn");

const closeCreateEventItemBtn =
    document.getElementById("closeCreateEventItemBtn");

const cancelCreateEventItemBtn =
    document.getElementById("cancelCreateEventItemBtn");

    const itemModalTitle =
    document.querySelector(".item-modal-title");


// ========================================
// ELEMENTOS adicionais do formulario
// ========================================

const itemCode =
    document.getElementById("item-code");
    
const codeProduct =
    document.getElementById("product-code");

const eventCode =
    document.getElementById("event-code");

const itemQuantity =
    document.getElementById("item-quantity");

// ========================================
// ABRIR MODAL
// ========================================

// openCreateProductBtn.addEventListener("click", () => {

//     createProductModal.classList.add("active");

// });


// ========================================
// FECHAR MODAL - BOTÃO X
// ========================================

closeCreateEventItemBtn.addEventListener("click", () => {

    createEventItemModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - BOTÃO CANCELAR
// ========================================

cancelCreateEventItemBtn.addEventListener("click", () => {

    createEventItemModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - CLICANDO FORA
// ========================================

createEventItemModal.addEventListener("click", (event) => {

    if (event.target === createEventItemModal) {

        createEventItemModal.classList.remove("active");

    }

});

// ========================================
// CRIAR PRODUTO
//========================================


createEventItemForm.addEventListener("submit", (event) => {

    event.preventDefault();

    const formData = new FormData(createEventItemForm);

    const client = {

        code: formData.get("item-code"),

        codeProduct: formData.get("product-code"),

        codeEvent: formData.get("event-code"),

        quantity: Number(formData.get("item-quantity")),
    };

});

let editingItemEventCode = null;

// ========================================
// Adicionar o cliente
// ========================================
openCreateEventItemBtn.addEventListener("click", () => {
    
    // Entrar no modo criação
    editingItemEventCode = null;

    // Limpar formulário
    createEventItemForm.reset();

    // Esconder código
    itemCode.hidden= true;


    // Alterar título;

    // Alterar título
    itemModalTitle.textContent =
        "Adicionar item ao evento";

    // Alterar botão

    // Abrir modal
    createEventItemModal.classList.add("active");
});

// ========================================
// EDIÇÃO
// ========================================


const editEventItemButtons =
    document.querySelectorAll(".editEventItemButtons");

editEventItemButtons.forEach(button => {

    button.addEventListener("click", () => {

        // ========================================
        // ENTRAR NO MODO EDIÇÃO
        // ========================================

        editingItemEventCode =
            button.dataset.code;


        // ========================================
        // MOSTRAR CÓDIGO
        // ========================================


        itemCode.value =
            button.dataset.code;

        

        // Código não pode ser alterado

        itemCode.readOnly = true;


        // ========================================
        // PREENCHER CAMPOS
        // ========================================

        eventCode.value =
            button.dataset.codeEvent;

        itemQuantity.value =
            button.dataset.quantity;
    


         codeProduct.value =
            button.dataset.codeProduct;
       
        // ========================================
        // ALTERAR TÍTULO
        // ========================================

        itemModalTitle.textContent =
            "Editar item do evento";


        // ========================================
        // ALTERAR BOTÃO
        // ========================================

        // createCategoryForm.textContent =
        //     "Guardar alterações";


        // ========================================
        // ABRIR MODAL
        // ========================================

        createEventItemModal.classList.add("active");

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

