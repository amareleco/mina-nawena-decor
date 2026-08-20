const stockMovementsTableBody =
    document.getElementById(
        "stock-movements-table-body"
    );

const createMovementForm =
    document.getElementById(
        "createMovementForm"
    )

const movementProductInput =
    document.getElementById(
        "movementProduct"
    );

const addMovementBtn =
    document.getElementById(
        "addMovementBtn"
    );

const cancelMovementBtn =
    document.getElementById(
        "cancelMovementBtn"
    );

const createMovementModal =
    document.getElementById(
        "createMovementModal"
    );

const closeCreateMovementBtn =
    document.getElementById(
        "closeCreateMovementBtn"

    )

const movementProductCodeInput =
    document.getElementById("movementProductCode");

const movementCodeGroup =
    document.getElementById("movementCodeGroup");

const movementTypeInput =
    document.getElementById(
        "movementType"
    )

const movementQuantityInput =
    document.getElementById(
        "movementQuantity"
    )

const movementReasonInput =
    document.getElementById(
        "movementReason"
    )

const movementCodeInput =
    document.getElementById(
        "movementCode"
    )

const movementTitleModal =
    document.querySelector(
        ".movement-modal-title"
    )

async function loadStockMovements() {

    try {

        const response = await fetch(
            `${API_URL}/stock-movements/`
        );

        if (!response.ok) {

            throw new Error(
                `Erro HTTP: ${response.status}`
            );

        }

        const movements =
            await response.json();

        stockMovementsData = movements;

        console.log(
            "Movimentos de stock:",
            movements
        );

        renderStockMovements(
            movements
        );

    } catch (error) {

        console.error(
            "Erro ao carregar movimentos:",
            error
        );

    }
}

function renderStockMovements(movements) {

    stockMovementsTableBody.innerHTML = "";

    movements.forEach(movement => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>
                ${movement.code}
            </td>

            <td>
                <strong>
                    ${movement.product_code}
                </strong>
                <br>
            </td>

            <td>
                    ${movement.product_name}
            </td>

            <td>
                ${movement.movement_type}
            </td>

            <td>
                ${movement.quantity}
            </td>

            <td>
                ${movement.reason ?? ""}
            </td>

            <td>
                ${movement.created_at ?? ""}
            </td>

            <td>
                ${movement.updated_at ?? ""}
            </td>

            <td class="actions text-center">

                <button
                    class="btn-action edit edit-stock-movement-btn"
                    title="Editar movimento"
                    data-code="${movement.code}"
                >
                    <i class="fas fa-pen"></i>
                </button>

                <button
                    class="btn-action delete delete-stock-movement-btn"
                    title="Apagar movimento"
                    data-code="${movement.code}"
                >
                    <i class="fas fa-trash-alt"></i>
                </button>

            </td>
        `;

        stockMovementsTableBody.appendChild(row);
    });
}

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadStockMovements();

    }
);

async function loadProductsForMovement() {

    try {

        const response = await apiFetch(
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
            "Produtos para movimento:",
            products
        );

        movementProductInput.innerHTML = `
            <option value="">
                Selecione um produto...
            </option>
        `;

        products.forEach(product => {

            console.log(
                "PRODUTO RECEBIDO:",
                product
            );

            const option =
                document.createElement("option");

            option.value =
                product.id;

            option.dataset.code =
                product.code;

            option.textContent =
                product.name;

            movementProductInput.appendChild(
                option
            );

        });

    } catch (error) {

        console.error(
            "ERRO AO CARREGAR PRODUTOS:",
            error
        );

    }
}
// post
const productSelect =
    document.getElementById("movementProduct");

console.log(
    "SELECT PRODUTO:",
    productSelect
);

console.log(
    "VALOR SELECIONADO:",
    productSelect.value
);

const productId =
    Number(productSelect.value);

console.log(
    "PRODUCT ID:",
    productId
);



createMovementForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        const movementData = {
            product_id: Number(movementProductInput.value),
            movement_type: movementTypeInput.value,
            quantity: Number(movementQuantityInput.value),
            reason: movementReasonInput.value.trim()
        };

        let url;
        let method;

        if (editingMovementCode) {

            // EDITAR
            url =
                `${API_URL}/stock-movements/${editingMovementCode}`;

            method = "PUT";

        } else {

            // CRIAR
            url =
                `${API_URL}/stock-movements/`;

            method = "POST";
        }

        console.log(
            "MÉTODO:",
            method
        );

        console.log(
            "URL:",
            url
        );

        console.log(
            "DADOS:",
            movementData
        );

        try {

            const response =
                await apiFetch(
                    url,
                    {
                        method: method,

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(
                                movementData
                            )
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
            await loadStockMovements();

            // Limpar formulário
            createMovementForm.reset();

            // Sair do modo edição
            editingMovementCode = null;

            // Fechar modal
            createMovementModal.classList.remove(
                "active"
            );

        } catch (error) {

            console.error(
                "ERRO:",
                error
            );
        }

    }
);

//abrir
addMovementBtn.addEventListener(
    "click",
    async () => {


         editingMovementCode = null;

        createMovementForm.reset();

        // Esconder código do movimento
        movementCodeGroup.style.display =
            "none";

        movementTitleModal.textContent =
            "Registo do Movimento do Estoque"

        // Limpar código do produto
        movementProductCodeInput.value = "";

        // Carregar produtos
        await loadProductsForMovement();

        // Abrir modal
        createMovementModal.classList.add(
            "active"
        );
    }
);

// cancelar
cancelMovementBtn.addEventListener("click", () => {

    createMovementModal.classList.remove(
        "active"
    );

});

closeCreateMovementBtn.addEventListener("click", () => {

    createMovementModal.classList.remove(
        "active"
    );

});


movementProductInput.addEventListener(
    "change",
    () => {

        const selectedOption =
            movementProductInput.selectedOptions[0];

        if (!selectedOption) {
            return;
        }

        movementProductCodeInput.value =
            selectedOption.dataset.code || "";

        console.log(
            "PRODUTO SELECIONADO:",
            selectedOption.textContent
        );

        console.log(
            "CÓDIGO:",
            selectedOption.dataset.code
        );

        console.log(
            "ID:",
            selectedOption.value
        );
    }
);

//put
let stockMovementsData = [];
let editingMovementCode = null;

stockMovementsTableBody.addEventListener(
    "click",
    async (event) => {

        const editButton =
            event.target.closest(
                ".edit-stock-movement-btn"
            );

        if (!editButton) {
            return;
        }

        const code =
            editButton.dataset.code;

            editingMovementCode = code

        const movement =
            stockMovementsData.find(
                item =>
                    item.code === code
            );

        if (!movement) {
            return;
        }

        console.log(
            "MOVIMENTO COMPLETO:",
            movement
        );


        // IMPORTANTE:
        // carregar os produtos ANTES
        // de tentar selecionar um deles

        await loadProductsForMovement();


        console.log(
            "OPTIONS DEPOIS DO LOAD:",
            [...movementProductInput.options].map(
                option => ({
                    value: option.value,
                    code: option.dataset.code,
                    name: option.textContent.trim()
                })
            )
        );


        // Procurar pelo código do produto

        const productOption =
            [...movementProductInput.options].find(
                option =>
                    option.dataset.code ===
                    movement.product_code
            );


        console.log(
            "OPTION ENCONTRADA:",
            productOption
        );


        if (productOption) {

            movementProductInput.value =
                productOption.value;

            movementProductCodeInput.value =
                movement.product_code;

        }


        // Preencher restantes campos

        movementCodeInput.value =
            movement.code;

        movementTypeInput.value =
            movement.movement_type;

        movementQuantityInput.value =
            movement.quantity;

        movementReasonInput.value =
            movement.reason || "";

        movementTitleModal.textContent =
            "Editar Movimento do Estoque"


        // Abrir modal

        createMovementModal.classList.add(
            "active"
        );

    }
);

stockMovementsTableBody.addEventListener(
    "click",
    async (event) => {

        const deleteButton =
            event.target.closest(
                ".delete-stock-movement-btn"
            );

        if (!deleteButton) {
            return;
        }

        const code =
            deleteButton.dataset.code;

        console.log(
            "ELIMINAR MOVIMENTO:",
            code
        );

        
        const confirmed =
            confirm(
                `Deseja eliminar o movimento ${code}?`
            );

        if (!confirmed) {
            return;
        }

        try {

            const response =
                await apiFetch(
                    `${API_URL}/stock-movements/${code}`,
                    {
                        method: "DELETE"
                    }
                );

            console.log(
                "DELETE STATUS:",
                response.status
            );

            const data =
                await response.json();

            console.log(
                "DELETE RESPOSTA:",
                data
            );

            if (!response.ok) {

                throw new Error(
                    JSON.stringify(data)
                );

            }

            // Atualizar tabela
            await loadStockMovements();

            console.log(
                "MOVIMENTO ELIMINADO COM SUCESSO"
            );

        } catch (error) {

            console.error(
                "ERRO AO ELIMINAR:",
                error
            );

        }

    }
);

// campo debusca
const searchMovement =
    document.getElementById("searchMovement");

    searchMovement.addEventListener(
    "input",
    () => {

        const search =
            searchMovement.value
                .toLowerCase()
                .trim();

        const filteredMovements =
            stockMovementsData.filter(
                movement => {

                    return (
                        movement.code
                            .toLowerCase()
                            .includes(search)

                        ||

                        movement.product_code
                            .toLowerCase()
                            .includes(search)

                        ||

                        movement.product_name
                            .toLowerCase()
                            .includes(search)

                        ||

                        movement.movement_type
                            .toLowerCase()
                            .includes(search)

                        ||

                        (movement.reason || "")
                            .toLowerCase()
                            .includes(search)
                    );

                }
            );

        renderStockMovements(
            filteredMovements
        );

    }
);