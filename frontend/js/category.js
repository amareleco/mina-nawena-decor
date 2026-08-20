// ======================================================
// CONFIGURAÇÃO
// ======================================================


// ======================================================
// ELEMENTOS DA PÁGINA
// ======================================================

const categoriesTableBody =
    document.getElementById("categories-table-body");


// ======================================================
// MODAL
// ======================================================

const createCategoryModal =
    document.getElementById("createCategoryModal");

const createCategoryForm =
    document.getElementById("createCategoryForm");


// ======================================================
// CAMPOS DO FORMULÁRIO
// ======================================================

const categoryCodeInput =
    document.getElementById("categoryCode");

const categoryNameInput =
    document.getElementById("categoryName");

const categoryDescriptionInput =
    document.getElementById("categoryDescription");


// ======================================================
// CONTROLES DO MODAL
// ======================================================

const openCreateCategoryBtn =
    document.getElementById("openCreateCategoryBtn");

const closeCreateCategoryBtn =
    document.getElementById("closeCreateCategoryBtn");

const cancelCreateCategoryBtn =
    document.getElementById("cancelCreateCategoryBtn");


// ======================================================
// TÍTULO E BOTÃO DO FORMULÁRIO
// ======================================================

const categoryModalTitle =
    document.querySelector(".categoryModalTitle");

const addCategoryBtn =
    document.getElementById("addCategoryBtn");


// ======================================================
// ESTADO DA EDIÇÃO
// ======================================================

// null = criando
// CAT-001 = editando

let editingCategoryCode = null;


// ======================================================
// DADOS RECEBIDOS DO BACKEND
// ======================================================

let categoriesData = [];


async function loadCategories() {

    try {

        const response = await fetch(
            `${API_URL}/categories/`
        );

        if (!response.ok) {

            throw new Error(
                `Erro HTTP: ${response.status}`
            );

        }

        const categories =
            await response.json();

        console.log(
            "Categorias recebidas:",
            categories
        );

        categoriesData = categories;

        renderCategories(categories);

    } catch (error) {

        console.error(
            "Erro ao carregar categorias:",
            error
        );

    }

}


function renderCategories(categories) {

    categoriesTableBody.innerHTML = "";

    categories.forEach(category => {

        const row =
            document.createElement("tr");

        row.innerHTML = `

            <td>
                ${category.code}
            </td>

            <td>
                <strong>
                    ${category.name}
                </strong>
            </td>

            <td>
                ${category.description ?? ""}
            </td>

            <td>
                ${category.created_at ?? ""}
            </td>

            <td class="actions text-center">

                <button
                    class="btn-action edit editCategoryButtons"
                    title="Editar Categoria"
                    data-code="${category.code}"
                >
                    <i class="fas fa-pen"></i>
                </button>

                <button
                    class="btn-action delete deleteCategoryButton"
                    title="Apagar Categoria"
                    data-code="${category.code}"
                >
                    <i class="fas fa-trash-alt"></i>
                </button>

            </td>

        `;

        categoriesTableBody.appendChild(row);

    });

}

openCreateCategoryBtn.addEventListener(
    "click",
    () => {

        editingCategoryCode = null;

        createCategoryForm.reset();

        categoryCodeInput.value = "";

        categoryCodeInput.hidden = true;

        categoryCodeInput.required = false;

        categoryModalTitle.textContent =
            "Adicionar categoria";

        addCategoryBtn.textContent =
            "Adicionar categoria";

        createCategoryModal.classList.add(
            "active"
        );

    }
);

closeCreateCategoryBtn.addEventListener(
    "click",
    () => {

        createCategoryModal.classList.remove(
            "active"
        );

    }
);

cancelCreateCategoryBtn.addEventListener("click", () => {

    createCategoryModal.classList.remove("active");

});

categoriesTableBody.addEventListener(
    "click",
    (event) => {

        const editButton =
            event.target.closest(
                ".editCategoryButtons"
            );

        if (!editButton) {
            return;
        }

        const code =
            editButton.dataset.code;

        console.log(
            "Editar categoria:",
            code
        );

        const category =
            categoriesData.find(
                item =>
                    item.code === code
            );

        if (!category) {

            console.error(
                "Categoria não encontrada:",
                code
            );

            return;
        }

        // ==============================
        // MODO EDIÇÃO
        // ==============================

        editingCategoryCode =
            category.code;

        // ==============================
        // PREENCHER CAMPOS
        // ==============================

        categoryCodeInput.value =
            category.code;

        categoryNameInput.value =
            category.name;

        categoryDescriptionInput.value =
            category.description ?? "";

        // ==============================
        // MOSTRAR CÓDIGO
        // ==============================

        categoryCodeInput.hidden = false;

        categoryCodeInput.required = true;

        // ==============================
        // ALTERAR TÍTULO
        // ==============================

        categoryModalTitle.textContent =
            "Editar categoria";

        // ==============================
        // ALTERAR BOTÃO
        // ==============================

        addCategoryBtn.textContent =
            "Guardar alterações";

        // ==============================
        // ABRIR MODAL
        // ==============================

        createCategoryModal.classList.add(
            "active"
        );

    }
);

createCategoryForm.addEventListener(
    "submit",
    (event) => {

        event.preventDefault();

        if (editingCategoryCode) {

            console.log(
                "MODO EDIÇÃO:",
                editingCategoryCode
            );

        } else {

            console.log(
                "MODO CRIAÇÃO"
            );

        }

    }
);

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadCategories();

    }
);


//=====================================================
// Post e edicao de categoria
//=====================================================

createCategoryForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const category = {
        name: categoryNameInput.value.trim(),
        description: categoryDescriptionInput.value.trim()
    };


    // ==================================================
    // EDITAR
    // ==================================================

    if (editingCategoryCode) {

        try {

            const response = await apiFetch(
                `${API_URL}/categories/${editingCategoryCode}`,
                {
                    method: "PUT",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(category)
                }
            );

            if (!response.ok) {

                const errorData =
                    await response.json();

                console.error(
                    "Erro do backend:",
                    errorData
                );

                throw new Error(
                    `Erro ao atualizar: ${response.status}`
                );
            }

            const updatedCategory =
                await response.json();

            console.log(
                "Categoria atualizada:",
                updatedCategory
            );

            createCategoryModal.classList.remove(
                "active"
            );

            createCategoryForm.reset();

            editingCategoryCode = null;

            await loadCategories();

        } catch (error) {

            console.error(
                "Erro ao atualizar categoria:",
                error
            );

        }

        return;
    }


    // ==================================================
    // CRIAR
    // ==================================================

    try {

        const response = await apiFetch(
            `${API_URL}/categories/`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(category)
            }
        );

        if (!response.ok) {

            const errorData =
                await response.json();

            console.error(
                "Erro do backend:",
                errorData
            );

            throw new Error(
                `Erro ao criar: ${response.status}`
            );
        }

        const newCategory =
            await response.json();

        console.log(
            "Categoria criada:",
            newCategory
        );

        createCategoryModal.classList.remove(
            "active"
        );

        createCategoryForm.reset();

        await loadCategories();

    } catch (error) {

        console.error(
            "Erro ao criar categoria:",
            error
        );

    }

});

//=====================================================
//Delete
//===================================================

categoriesTableBody.addEventListener("click", async (event) => {

    const deleteButton =
        event.target.closest(".deleteCategoryButton");

    if (!deleteButton) {
        return;
    }

    const code =
        deleteButton.dataset.code;

    console.log(
        "Categoria para apagar:",
        code
    );


    const confirmed =
        confirm(
            `Tem certeza que deseja apagar a categoria ${code}?`
        );

    if (!confirmed) {
        return;
    }


    try {

        const response = await apiFetch(
            `${API_URL}/categories/${code}`,
            {
                method: "DELETE"
            }
        );


        if (!response.ok) {

            const errorData =
                await response.json();

            console.error(
                "Erro do backend:",
                errorData
            );

            throw new Error(
                `Erro ao apagar: ${response.status}`
            );
        }


        console.log(
            "Categoria apagada:",
            code
        );


        await loadCategories();


    } catch (error) {

        console.error(
            "Erro ao apagar categoria:",
            error
        );

    }

});

// campo de busca

categorySearch.addEventListener("input", () => {

    const searchTerm =
        categorySearch.value
            .trim()
            .toLowerCase();

    const filteredCategories =
        categoriesData.filter(category => {

            return (
                category.code
                    ?.toLowerCase()
                    .includes(searchTerm)

                ||

                category.name
                    ?.toLowerCase()
                    .includes(searchTerm)

                ||

                category.description
                    ?.toLowerCase()
                    .includes(searchTerm)
            );

        });

    renderCategories(filteredCategories);

});