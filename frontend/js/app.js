(function() {
    'use strict';
    const form = document.getElementById('form');

    function request(url) {
        return fetch(url).then(response => response.json());
    }

    function change_list_content(list, element) {
        const li = list.reduce((elements, value) => {
            return elements + `<li>${value}</li>`;
        }, "");
        element.innerHTML = li;
    }

    function change_explication_content(neighbors) {
        const explication_text = document.getElementById('explication_text');
        const neighbors_element = document.getElementById('neighbors');
        const explication = "Esses são o usuários mais similares a você "
                        + "com a nota desses usuários foi feita a recomendação mais "
                        + "similar ao seu perfil. "
                        + "Os filmes recomendados são os que possuem as maiores notas "
                        + "atribuidas por estes usuários. "
                        + "Os 3 usuários estão listados abaixo";
        
        explication_text.innerText = explication;
        change_list_content(neighbors, neighbors_element);
    }

    function get_results() {
        const movies = document.getElementById('movies');
        const rmse = document.getElementById('rmse');
        request(`/api/results?uid=${form.user.value}`).then(data => {
            change_list_content(data.result, movies);
            change_explication_content(data.neighbors);
            rmse.innerText = `RMSE: ${data.rmse}`;
        });
        return false;
    }


    (function main() {
        form.onsubmit = get_results;
        request('/api/users').then(data => {
            const usersSelect = document.getElementById('users');
            const options = data.users_id.reduce((options, userId) => {
                return options + `<option value=${userId}>${userId}</option>`;
            }, usersSelect.innerHTML);

            usersSelect.innerHTML = options;
        });
    })();
})();
