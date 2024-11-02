function filtrarPorCategoria(selectElement) {
    const categoriaId = selectElement.value;
    if (categoriaId) {
        window.location.href = `/category/filter/?categoria_id=${categoriaId}`;
    }
}