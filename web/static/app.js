document.getElementById('scrapeButton').addEventListener('click', scrapeWiki);
document.getElementById('searchButton').addEventListener('click', searchText);

function scrapeWiki() {
    const target = document.getElementById('wikiUrl').value;
    console.log("target");
    fetch(`/scrape?target=${target}`)
        .then(response => console.log(response)); 
}

function searchText() {
    const query = document.getElementById('searchQuery').value;
    fetch(`/search?query=${query}`)
        .then(response => response.text())
        .then(result => {
            document.getElementById('searchResult').textContent = result;
        });
}
