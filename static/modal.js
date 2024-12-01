const exampleModal = document.getElementById("exampleModal");
if (exampleModal) {
  exampleModal.addEventListener("show.bs.modal", (event) => {
    // Button that triggered the modal
    const button = event.relatedTarget;
    // Extract info from data-bs-* attributes
    const recipient = button.getAttribute("data-bs-whatever");
    const speciesData = button.getAttribute("data-bs-species");
    const scientificData = button.getAttribute("data-bs-scientific_name");
    const shapeData = button.getAttribute("data-bs-shape");
    const waterData = button.getAttribute("data-bs-water_type");
    const lengthData = button.getAttribute("data-bs-avg_length");
    const lifeData = button.getAttribute("data-bs-avg_lifespan");
    const legsData = button.getAttribute("data-bs-has_legs");
    const idData = button.getAttribute("data-bs-id");
    // If necessary, you could initiate an Ajax request here
    // and then do the updating in a callback.

    // Update the modal's content.
    const modalTitle = exampleModal.querySelector(".modal-title");
    const species = exampleModal.querySelector("#species");
    const scientific_name = exampleModal.querySelector("#scientific_name");
    const shape = exampleModal.querySelector("#shape");
    const water_type = exampleModal.querySelector("#water_type");
    const avg_length = exampleModal.querySelector("#avg_length");
    const avg_lifespan = exampleModal.querySelector("#avg_lifespan");
    const has_legs = exampleModal.querySelector("#has_legs");
    const del = exampleModal.querySelector("#delete");
    const update = exampleModal.querySelector("#update");

    modalTitle.textContent = `${recipient}`;
    species.textContent = `${speciesData}`;
    scientific_name.textContent = `${scientificData}`;
    shape.textContent = `${shapeData}`;
    water_type.textContent = `${waterData}`;
    avg_length.textContent = `${lengthData}cm`;
    avg_lifespan.textContent = `${lifeData} years`;
    has_legs.textContent = `${legsData}`;
    del.setAttribute("href", `/delete?id=${idData}`);
    update.setAttribute("href", `/update?id=${idData}`);
  });
}
