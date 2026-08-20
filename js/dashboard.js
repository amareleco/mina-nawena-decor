console.log("Hello, world!");

async function loadDashboard() {

    try {

        const token =
            localStorage.getItem("access_token");

        if (!token) {
            window.location.href = "login.html";
            return;
        }

        const response = await fetch(
            `${API_URL}/dashboard/`,
            {
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            }
        );

        if (response.status === 401) {
            localStorage.removeItem("access_token");
            window.location.href = "login.html";
            return;
        }

        if (!response.ok) {
            throw new Error(
                `Erro HTTP: ${response.status}`
            );
        }

        const data =
            await response.json();

        console.log(
            "DADOS DO DASHBOARD:",
            data
        );

        renderDashboard(data);

    } catch (error) {

        console.error(
            "Erro ao carregar dashboard:",
            error
        );

    }
}

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadDashboard();

    }
);


document.getElementById("low-stock");


 function renderDashboard(data) {

    // Cards
    document.getElementById("total-products").textContent =
        data.totals.products;

    document.getElementById("total-categories").textContent =
        data.totals.categories;

    // Movimentações
    renderMovements(data.recent_movements);

    // Estoque baixo
    renderLowStock(data.low_stock);
}

//Produtos

// function renderProducts(products) {

//     const tbody =
//         document.getElementById(
//             "dashboard-products-body"
//         );

//     tbody.innerHTML = "";

//     products.forEach(product => {

//         const row =
//             document.createElement("tr");

//         row.innerHTML = `
//             <td>
//                 ${product.code}
//             </td>

//             <td>
//                 ${product.name}
//             </td>

//             <td>
//                 ${product.quantity}
//             </td>
//         `;

//         tbody.appendChild(row);

//     });
// }

//Movimentos

 function renderMovements(movements) {

    const tbody = document.getElementById("recent-movements-body");

    if (!tbody) {
        console.warn(
            "Elemento #recent-movements-body não encontrado."
        );
        return;
    }

    tbody.innerHTML = "";

    if (!movements || movements.length === 0) {

        tbody.innerHTML = `
            <tr>
                <td colspan="6" class="empty-state">
                    Nenhuma movimentação recente.
                </td>
            </tr>
        `;

        return;
    }

    movements.forEach(movement => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${movement.code}</td>
            <td>${movement.product_code}</td>
            <td>${movement.product_name}</td>
            <td>${movement.movement_type}</td>
            <td>${movement.quantity}</td>
            <td>${movement.created_at}</td>
        `;

        tbody.appendChild(row);
    });
}



// baixo estoque
function renderLowStock(products) {

    const container = document.getElementById("low-stock");

    if (!container) {
        console.warn(
            "Elemento #low-stock não encontrado."
        );
        return;
    }

    container.innerHTML = "";

    if (!products || products.length === 0) {

        container.innerHTML = `
            <div class="empty-state">
                Nenhum produto com estoque baixo.
            </div>
        `;

        return;
    }

    products.forEach(product => {

        const item = document.createElement("tr");

        item.className = "low-stock-item";

        item.innerHTML = `
            <td>${product.code}</td>
            <td><strong>${product.name}</strong></td>
            <td>${product.quantity}</td>
        `;

        container.appendChild(item);
    });
}

//event

// function renderRecentEvents(events) {

//     const tbody =
//         document.getElementById(
//             "recent-events-body"
//         );

//     tbody.innerHTML = "";

//     events.forEach(event => {

//         const row =
//             document.createElement("tr");

//         row.innerHTML = `
//             <td>
//                 ${event.code}
//             </td>

//             <td>
//                 ${event.client_name}
//             </td>

//             <td>
//                 ${event.event_date}
//             </td>
//         `;

//         tbody.appendChild(row);

//     });
// }

// cards
const totalProducts =
    document.getElementById("total-products");

const totalCategories =
    document.getElementById("total-categories");

// requicoes
