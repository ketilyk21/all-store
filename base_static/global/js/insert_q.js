document.getElementById('searchForm').addEventListener('submit', function(event) {
    var query = document.querySelector('input[name="q"]').value;
    var currentUrl = window.location.href.split('?')[0]; // Remove current query parameters
    var queryString = new URLSearchParams(window.location.search);
    
    // Set the 'q' parameter (or update if it exists)
    queryString.set('q', query);
    
    // Append the updated query string
    this.action = currentUrl + '?' + queryString.toString();
});