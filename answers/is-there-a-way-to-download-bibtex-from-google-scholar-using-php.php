// https://stackoverflow.com/questions/8217769/is-there-a-way-to-download-bibtex-from-google-scholar-using-php/23176299#23176299
// https://replit.com/@DimitryZub1/is-there-a-way-to-download-bibtex-from-google-scholar-php-1#main.php

<?php
ini_set("display_errors", 1);
ini_set("display_startup_errors", 1);
error_reporting(E_ALL);

require __DIR__ . "/vendor/autoload.php";

function getResultIds () {
    $result_ids = array();

    $params = [
        "engine" => "google_scholar", // parsing engine
        "q" => "biology"              // search query
    ];

    $search = new GoogleSearch(getenv("API_KEY"));
    $response = $search->get_json($params);

    foreach ($response->organic_results as $result) {
        // print_r($result->result_id);

        array_push($result_ids, $result->result_id);
    }

    return $result_ids;
}

function getBibtexData () {
    $bibtex_data = array();

    foreach (getResultIds() as $result_id) {
        $params = [
            "engine" => "google_scholar_cite",  // parsing engine
            "q" => $result_id
        ];

        $search = new GoogleSearch(getenv("API_KEY"));
        $response = $search->get_json($params);

        foreach ($response->links as $result) {
            if ($result->name === "BibTeX") {
                array_push($bibtex_data, $result->link);
            }
        }
    }

    return $bibtex_data;
}

print_r(json_encode(getBibtexData(), JSON_PRETTY_PRINT));
?>