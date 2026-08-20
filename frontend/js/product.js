console.log("Products JS carregado");


// ======================================================
// CONFIGURAÇÃO
// ======================================================

// ======================================================
// TABELA
// ======================================================

const productsTableBody =
    document.getElementById("products-table-body");


// ======================================================
// DADOS
// ======================================================

let productsData = [];


// ======================================================
// CARREGAR PRODUTOS
// ======================================================

async function loadProducts() {

    try {

        const response = await fetch(
            `${API_URL}/products/`
        );

        if (!response.ok) {

            throw new Error(
                `Erro HTTP: ${response.status}`
            );

        }

        const products =
            await response.json();

        console.log(
            "Produtos recebidos:",
            products
        );

        console.log(
            "Quantidade:",
            products.length
        );

        productsData = products;

        renderProducts(products);

    } catch (error) {

        console.error(
            "Erro ao carregar produtos:",
            error
        );

    }

}

function formatPrice(price) {
    return Number(price).toLocaleString("pt-MZ", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }) + " MT";
}


function renderProducts(products) {

    productsTableBody.innerHTML = "";

    products.forEach(product => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${product.code ?? ""}</td>

            <td>
                <strong>
                    ${product.name ?? ""}
                </strong>
            </td>

            <td>
                ${product.category.name ?? ""}
            </td>

            <td>
                ${product.description ?? ""}
            </td>

            <td>
                ${product.quantity ?? 0}
            </td>

            <td>
                ${product.minimum_stock ?? 0}
            </td>

            <td>
                ${product.is_active? "Disponível" : "Indisponível"}
            </td>

            <td>
                ${product.created_at ?? ""}
            </td>

            <td class="actions text-center">

                <button
                    type="button"
                    class="btn-action edit edit-product-btn"
                    title="Editar Produto"
                    data-code="${product.code}"
                >
                    <i class="fas fa-pen"></i>
                </button>

                <button
                    type="button"
                    class="btn-action delete delete-product-btn"
                    title="Apagar Produto"
                    data-code="${product.code}"
                >
                    <i class="fas fa-trash-alt"></i>
                </button>

            </td>
        `;

        productsTableBody.appendChild(row);

    });

}


// ======================================================
// INICIALIZAÇÃO
// ======================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadProducts();

    }
);

//==================================================
// ELEMENTOS DE MODAL
//=================================================

const createProductModal =
    document.getElementById("createProductModal");

const createProductForm =
    document.getElementById("createProductForm");


const productCodeInput = 
    document.getElementById("productCode")

const productNameInput =
    document.getElementById("productName");

const productDescriptionInput =
    document.getElementById("productDescription");

const productCategoryInput =
    document.getElementById("productCategory");

const productQuantityInput =
    document.getElementById("productQuantity");

const productMinimumStockInput =
    document.getElementById("productMinimumStock");

const productStateInput =
    document.getElementById("productState");

const openCreateProductBtn =
    document.getElementById("openCreateProductBtn");

const productModalTitle =
    document.querySelector(".productModalTitle");

const addProductBtn =
    document.getElementById("addProductBtn");

const closeCreateProductBtn =
        document.getElementById("closeCreateProductBtn");

const cancelCreateProductBtn =
    document.getElementById("cancelCreateProductBtn");

const productSearch =
    document.getElementById("productSearch");

let editingProductCode = null;



// POST e PUT
createProductForm.addEventListener("submit", async (event) => {createProductForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        const formData =
            new FormData(
                createProductForm
            );

        const product = {

            name:
                formData
                    .get("name")
                    ?.trim() || "",

            description:
                formData
                    .get("description")
                    ?.trim() || "",

            category_id:
                Number(
                    formData.get(
                        "categoryId"
                    )
                ),

            quantity:
                Number(
                    formData.get(
                        "quantity"
                    )
                ),

            minimum_stock:
                Number(
                    formData.get(
                        "minimum_stock"
                    )
                ),

            is_active:
                formData.get(
                    "is_active"
                ) === "true"
        };

        try {

            let response;

            // ==========================
            // PUT
            // ==========================

            if (editingProductCode) {

                response = await apiFetch(
                    `${API_URL}/products/${editingProductCode}`,
                    {
                        method: "PUT",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(
                                product
                            )
                    }
                );

            }

            // ==========================
            // POST
            // ==========================

            else {

                response = await apiFetch(
                    `${API_URL}/products/`,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(
                                product
                            )
                    }
                );
            }

            const data =
                await response.json();

            console.log(
                "Resposta:",
                data
            );

            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    `Erro HTTP: ${response.status}`
                );
            }

            // fechar modal
            createProductModal.classList.remove(
                "active"
            );

            // limpar formulário
            createProductForm.reset();

            // voltar para modo criação
            editingProductCode = null;

            addProductBtn.textContent =
                "Adicionar produto";

            productModalTitle.textContent =
                "Novo produto";

            // atualizar tabela
            await loadProducts();

        } catch (error) {

            console.error(
                "Erro ao salvar produto:",
                error
            );
        }
    }
);

    event.preventDefault();

    console.log("1 - SUBMIT DISPARADO");

    const formData = new FormData(createProductForm);

    // Verificar categoria
    const selectedCategory =
        formData.get("category_id");

    console.log(
        "CATEGORY ID:",
        selectedCategory
    );

    if (!selectedCategory) {
        alert("Selecione uma categoria.");
        return;
    }

    const categoryId =
        Number(selectedCategory);

    if (Number.isNaN(categoryId)) {
        alert("Categoria inválida.");
        return;
    }


    // teste
    const selectedCategories =
        formData.get("category_id");

        console.log(
            "CATEGORY ID RECEBIDO DO FORM:",
            selectedCategories
        );

        console.log(
            "SELECT VALUE:",
            productCategoryInput.value
        );

        console.log(
            "SELECT NAME:",
            productCategoryInput.name
    );
    

    // Montar produto
    const product = {

        name:
            formData.get("name")?.trim() || "",

        description:
            formData.get("description")?.trim() || "",

        category_id:
            categoryId,

        quantity:
            Number(
                formData.get("quantity")
            ),

        minimum_stock:
            Number(
                formData.get("minimum_stock")
            ),

        is_active:
            formData.get("is_active") === "true"
    };

    console.log(
        "2 - PRODUTO:",
        JSON.stringify(
            product,
            null,
            2
        )
    );
    

    try {

        console.log(
            "3 - VOU FAZER O FETCH"
        );

        const response = await apiFetch(
            `${API_URL}/products/`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body:
                    JSON.stringify(product)
            }
        );

        console.log(
            "4 - STATUS:",
            response.status
        );

        const data =
            await response.json();

        console.log(
            "5 - RESPOSTA:",
            JSON.stringify(
                data,
                null,
                2
            )
        );

        if (!response.ok) {

            throw new Error(
                `Erro HTTP: ${response.status}`
            );

        }

        console.log(
            "6 - PRODUTO CRIADO!"
        );

        createProductForm.reset();

        createProductModal.classList.remove(
            "active"
        );

        await loadProducts();

    } catch (error) {

        console.error(
            "ERRO NO POST:",
            error
        );

    }

});


// CATEGORIAS
async function loadCategoriesForProduct() {

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
            "Categorias para produto:",
            categories
        );


        // Limpar opções existentes
        productCategoryInput.innerHTML = `
            <option value="">
                Selecione uma categoria...
            </option>
        `;


        // Adicionar todas as categorias
        categories.forEach(category => {

            const option =
                document.createElement("option");

            option.value =
                category.id;

            option.textContent =
                category.name;

            productCategoryInput.appendChild(
                option
            );

        });


    } catch (error) {

        console.error(
            "Erro ao carregar categorias:",
            error
        );

    }

}

document.addEventListener(
    "DOMContentLoaded",
    async () => {

        await loadProducts();

        await loadCategoriesForProduct();

    }
);

// ======================================================
// ABRIR MODAL — CRIAR PRODUTO
// ======================================================

openCreateProductBtn.addEventListener("click", () => {

    // Garantir que estamos no modo criação
    editingProductCode = null;

    // Limpar formulário
    createProductForm.reset();

    productCodeInput.hidden = true;

        productCodeInput.required = false

    // Título
    productModalTitle.textContent =
        "Adicionar produto";

    // Botão
    addProductBtn.textContent =
        "Adicionar produto";

    // Abrir modal
    createProductModal.classList.add("active");

});

closeCreateProductBtn.addEventListener(
    "click",
    () => {

        createProductModal.classList.remove(
            "active"
        );

    }
);

cancelCreateProductBtn.addEventListener("click", () => {

    createProductModal.classList.remove("active");

});

//edicao
productsTableBody.addEventListener(
    "click",
    async (event) => {

        const editButton =
            event.target.closest(
                ".edit-product-btn"
            );

        if (!editButton) {
            return;
        }

        const code =
            editButton.dataset.code;

        console.log(
            "Editar produto:",
            code
        );

        const product =
            productsData.find(
                item =>
                    item.code === code
            );

        if (!product) {
            console.error(
                "Produto não encontrado:",
                code
            );

            return;
        }

        editingProductCode =
            product.code;

        // preencher campos

        productCodeInput.value =
            product.code;
        productNameInput.value =
            product.name;

        productDescriptionInput.value =
            product.description ?? "";

        productCategoryInput.value =
            product.category.id;

        productQuantityInput.value =
            product.quantity;

        productMinimumStockInput.value =
            product.minimum_stock;

        productStateInput.value =
            String(product.is_active);

        // mudar título
        productModalTitle.textContent =
            "Editar produto";

        // mudar botão
        addProductBtn.textContent =
            "Guardar alterações";

        // abrir modal
        createProductModal.classList.add(
            "active"
        );
    }
);


// Deletar um produto
productsTableBody.addEventListener(
    "click",
    async (event) => {

        const deleteButton =
            event.target.closest(
                ".delete-product-btn"
            );

        if (!deleteButton) {
            return;
        }

        const code =
            deleteButton.dataset.code;

        console.log(
            "Apagar produto:",
            code
        );

        const confirmed =
            confirm(
                `Deseja realmente apagar o produto ${code}?`
            );

        if (!confirmed) {
            return;
        }

       try {

    const response = await apiFetch(
        `${API_URL}/products/${code}`,
        {
            method: "DELETE"
        }
    );

    console.log(
        "DELETE STATUS:",
        response.status
    );

    if (!response.ok) {

        const errorData =
            await response.text();

        throw new Error(
            errorData ||
            `Erro HTTP: ${response.status}`
        );
    }

    console.log(
        `Produto ${code} eliminado com sucesso.`
    );

    await loadProducts();

} catch (error) {

    console.error(
        "Erro ao apagar produto:",
        error
    );

}

}
    
);

// campo de busca

productSearch.addEventListener("input", () => {

    const search =
        productSearch.value
            .trim()
            .toLowerCase();

    const filteredProducts =
        productsData.filter(product => {

            return (
                product.code
                    ?.toLowerCase()
                    .includes(search)

                ||

                product.name
                    ?.toLowerCase()
                    .includes(search)

                ||

                product.category?.name
                    ?.toLowerCase()
                    .includes(search)
            );

        });

    renderProducts(filteredProducts);

});