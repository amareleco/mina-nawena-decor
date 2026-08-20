console.log("Hello, world!");



// ========================================
// ELEMENTOS DO MODAL
// ========================================

const createEventModal =
    document.getElementById("createEventModal");

const createEventForm =
    document.getElementById("createEventForm");

const openCreateEventBtn =
    document.getElementById("openCreateEventBtn");

const closeCreateEventBtn =
    document.getElementById("closeCreateEventBtn");

const cancelCreateEventBtn =
    document.getElementById("cancelCreateEventBtn");


// ========================================
// ELEMENTOS adicionais do formulario
// ========================================

const eventCode =
    document.getElementById("event-code");
    
const eventName =
    document.getElementById("event-name");

const ClientCode =
    document.getElementById("client-code");

const eventType =
    document.getElementById("event-type");

const eventLocation =
    document.getElementById("event-location");

const eventDescription =
    document.getElementById("event-description");

const eventStatus =
    document.getElementById("event-status");

const eventModalTitle =
    document.querySelector(".event-modal-title");

    const dataCreeatedTitle =
    document.querySelector(".data-created-title");

const addEventBtn =
    document.querySelector(".event-modal-title");

const dataCreated =
    document.getElementById("event-created-at");


// ========================================
// ABRIR MODAL
// ========================================

// openCreateProductBtn.addEventListener("click", () => {

//     createProductModal.classList.add("active");

// });


// ========================================
// FECHAR MODAL - BOTÃO X
// ========================================

closeCreateEventBtn.addEventListener("click", () => {

    createEventModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - BOTÃO CANCELAR
// ========================================

cancelCreateEventBtn.addEventListener("click", () => {

    createEventModal.classList.remove("active");

});


// ========================================
// FECHAR MODAL - CLICANDO FORA
// ========================================

createEventModal.addEventListener("click", (event) => {

    if (event.target === createEventModal) {

        createEventModal.classList.remove("active");

    }

});

// ========================================
// CRIAR PRODUTO
//========================================


createEventForm.addEventListener("submit", (event) => {

    event.preventDefault();

    const formData = new FormData(createEventForm);

    const client = {

        code: formData.get("event-code"),

        name: formData.get("event-name"),

        location: formData.get("event-location"),

        description: formData.get("event-description"),

        type: formData.get("event-type"),

        eventStatus: formData.get("event-status"),

        clinetCode: formData.get("client-code"),

        dataAtualizacao: new Date().toISOString().split("T")[0],

        dataCriacao: new Date().toISOString().split("T")[0]

    };

});

let editingClientCode = null;

// ========================================
// Adicionar o cliente
// ========================================
openCreateEventBtn.addEventListener("click", () => {
    
    // Entrar no modo criação
    editingClientCode = null;

    // Limpar formulário
    createEventForm.reset();

    // Esconder código
    eventCode.hidden= true;

    //Esconder a data de criacao
    dataCreated.hidden= true;

    // Alterar título;

    // Alterar título
    eventModalTitle.textContent =
        "Adicionar evento";

    // Alterar botão

    // Abrir modal
    createEventModal.classList.add("active");
});

// ========================================
// EDIÇÃO
// ========================================


const editEventButtons =
    document.querySelectorAll(".editEventButtons");

editEventButtons.forEach(button => {

    button.addEventListener("click", () => {

        // ========================================
        // ENTRAR NO MODO EDIÇÃO
        // ========================================

        editingClientCode =
            button.dataset.code;


        // ========================================
        // MOSTRAR CÓDIGO
        // ========================================


        eventCode.value =
            button.dataset.code;


        // Código não pode ser alterado

        eventCode.readOnly = true;


      //Esconder a data de criacao
      dataCreated.hidden= true;




        // ========================================
        // PREENCHER CAMPOS
        // ========================================

        
         eventType.value =
            button.dataset.type;

        eventName.value =
            button.dataset.name;
        
         eventLocation.value =
            button.dataset.location;


         eventDescription.value =
            button.dataset.description;
       
        // ========================================
        // ALTERAR TÍTULO
        // ========================================

        eventModalTitle.textContent =
            "Editar evento";


        dataCreeatedTitle.textContent =
            "Data de atualizcao do evento"


        // ========================================
        // ALTERAR BOTÃO
        // ========================================

        // createCategoryForm.textContent =
        //     "Guardar alterações";


        // ========================================
        // ABRIR MODAL
        // ========================================

        createEventModal.classList.add("active");

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

