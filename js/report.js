/* ==========================================================
   INICIALIZAÇÃO
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    loadReport("products");

});


/* ==========================================================
   CARREGAR RELATÓRIO
========================================================== */

async function loadReport(type) {

    if (type === "products") {

        await loadProductsReport();

    }

    else if (type === "movements") {

        await loadMovementsReport();

    }

}


/* ==========================================================
   RELATÓRIO DE PRODUTOS
========================================================== */

async function loadProductsReport() {

    const tbody =
        document.getElementById("products-report-body");

    try {

        /*
         * Estado de carregamento
         */

        tbody.innerHTML = `
            <tr>
                <td colspan="8" class="report-loading">
                    Carregando produtos...
                </td>
            </tr>
        `;


        /*
         * Requisição ao backend
         */

        const response = await fetch(
            `${API_URL}/reports/products`
        );


        /*
         * Verificar resposta HTTP
         */

        if (!response.ok) {

            throw new Error(
                `Erro HTTP: ${response.status}`
            );

        }


        /*
         * Converter resposta para JSON
         */

        const report =
            await response.json();


        console.log(
            "RELATÓRIO DE PRODUTOS:",
            report
        );


        /*
         * Atualizar cabeçalho
         */

        updateReportHeader(
            report.header
        );


        /*
         * Renderizar produtos
         */

        renderProductsReport(
            report.data
        );


    }

    catch (error) {

        console.error(
            "Erro ao carregar relatório de produtos:",
            error
        );


        tbody.innerHTML = `
            <tr>
                <td colspan="8" class="report-error">
                    Erro ao carregar o relatório de produtos.
                </td>
            </tr>
        `;

    }

}


/* ==========================================================
   RENDERIZAR PRODUTOS
========================================================== */

function renderProductsReport(products) {

    const tbody =
        document.getElementById(
            "products-report-body"
        );


    /*
     * Verificar se existem produtos
     */

    if (
        !products ||
        products.length === 0
    ) {

        tbody.innerHTML = `
            <tr>
                <td colspan="8" class="report-empty">
                    Nenhum produto encontrado.
                </td>
            </tr>
        `;

        return;

    }


    /*
     * Limpar tabela
     */

    tbody.innerHTML = "";


    /*
     * Criar cada linha
     */

    products.forEach(product => {

        const row =
            document.createElement("tr");


        /*
         * Estado do estoque
         */

        const stockStatus =
            getStockStatus(
                product.stock_status
            );


        row.innerHTML = `

            <td>
                <span class="badge-code">
                    ${escapeHTML(product.code)}
                </span>
            </td>

            <td>
                ${escapeHTML(product.name)}
            </td>

            <td>
                ${escapeHTML(product.category_code)}
            </td>

            <td>
                ${escapeHTML(product.category_name)}
            </td>

            <td>
                ${product.quantity}
            </td>

            <td>
                ${product.minimum_stock}
            </td>

            <td>
                <span class="badge-status ${stockStatus.className}">
                    ${escapeHTML(stockStatus.label)}
                </span>
            </td>

        `;


        tbody.appendChild(row);

    });

}


/* ==========================================================
   STATUS DO STOCK
========================================================== */

function getStockStatus(status) {

    const normalized =
        String(status || "")
            .trim()
            .toUpperCase();

    switch (normalized) {

        case "IN STOCK":

            return {
                label: "EM STOCK",
                className: "active"
            };


        case "LOW STOCK":

            return {
                label: "STOCK BAIXO",
                className: "inactive"
            };


        case "OUT OF STOCK":

            return {
                label: "ESGOTADO",
                className: "inactive"
            };


                default:

                    return {
                        label: normalized || "DESCONHECIDO",
                        className: "inactive"
                    };

            }

        }


/* ==========================================================
   ATUALIZAR HEADER DO RELATÓRIO
========================================================== */

function updateReportHeader(header) {

    if (!header) {

        return;

    }


    document.getElementById(
        "header-company"
    ).textContent =
        header.company || "-";


    document.getElementById(
        "header-report-name"
    ).textContent =
        header.report_name || "-";


    document.getElementById(
        "header-generated-at"
    ).textContent =
        formatDateTime(header.generated_at);


    document.getElementById(
        "header-total-records"
    ).textContent =
        header.total_records ?? 0;

}


/* ==========================================================
   FORMATAR DATA
========================================================== */

function formatDateTime(value) {

    if (!value) {

        return "-";

    }


    const date =
        new Date(value);


    if (isNaN(date.getTime())) {

        return value;

    }


    return date.toLocaleString(
        "pt-PT",
        {
            day: "2-digit",
            month: "2-digit",
            year: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        }
    );

}


/* ==========================================================
   FORMATAR PREÇO
========================================================== */

function formatCurrency(value) {

    if (
        value === null ||
        value === undefined ||
        value === ""
    ) {

        return "-";

    }


    const number =
        Number(value);


    if (isNaN(number)) {

        return `${escapeHTML(value)} MT`;

    }


    return number.toLocaleString(
        "pt-MZ",
        {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        }
    ) + " MT";

}


/* ==========================================================
   PROTEÇÃO CONTRA HTML INJETADO
========================================================== */

function escapeHTML(value) {

    if (
        value === null ||
        value === undefined
    ) {

        return "";

    }


    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}


/* ==========================================================
   RELATÓRIO DE MOVIMENTOS
========================================================== */

async function loadMovementsReport() {

    const tbody =
        document.getElementById(
            "movements-report-body"
        );


    try {

        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="report-loading">
                    Carregando movimentos...
                </td>
            </tr>
        `;


        const response = await fetch(
            `${API_URL}/reports/movements`
        );


        if (!response.ok) {

            throw new Error(
                `Erro HTTP: ${response.status}`
            );

        }


        const report =
            await response.json();


        console.log(
            "RELATÓRIO DE MOVIMENTOS:",
            report
        );


        /*
         * Atualizar cabeçalho
         */

        updateReportHeader(
            report.header
        );


        /*
         * Renderizar movimentos
         */

        renderMovementsReport(
            report.data
        );


    }

    catch (error) {

        console.error(
            "Erro ao carregar relatório de movimentos:",
            error
        );


        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="report-error">
                    Erro ao carregar o relatório de movimentos.
                </td>
            </tr>
        `;

    }

}


/* ==========================================================
   RENDERIZAR MOVIMENTOS
========================================================== */

function renderMovementsReport(movements) {

    const tbody =
        document.getElementById(
            "movements-report-body"
        );


    if (
        !movements ||
        movements.length === 0
    ) {

        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="report-empty">
                    Nenhum movimento encontrado.
                </td>
            </tr>
        `;

        return;

    }


    tbody.innerHTML = "";


    movements.forEach(movement => {

        const row =
            document.createElement("tr");


        /*
         * Determinar classe do movimento
         */

        const movementType =
            String(
                movement.movement_type || ""
            )
            .trim()
            .toUpperCase();


        let movementClass =
            "movement-in";


        if (
            movementType === "SAIDA" ||
            movementType === "SAÍDA" ||
            movementType === "DANIFICADO"

        ) {

            movementClass =
                "movement-out";

        }


        row.innerHTML = `

            <td>
                <span class="badge-code">
                    ${escapeHTML(movement.code)}
                </span>
            </td>

            <td>
                ${escapeHTML(movement.product_code)}
            </td>

            <td>
                ${escapeHTML(movement.product_name)}
            </td>

            <td>
                <span class="badge-status ${movementClass}">
                    ${escapeHTML(movement.movement_type)}
                </span>
            </td>

            <td>
                ${movement.quantity}
            </td>

            <td>
                ${escapeHTML(movement.reason || "-")}
            </td>

            <td>
                ${formatDateTime(movement.created_at)}
            </td>

        `;


        tbody.appendChild(row);

    });

}