<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

require __DIR__ . '/vendor/autoload.php';

$queries = array(
    "moon",
    "pandas",
    "python",
    "data science",
    "ML",
    "AI",
    "animals",
    "amd",
    "nvidia",
    "intel",
    "asus",
    "robbery pi",
    "latex, tex",
    "amg",
    "blizzard",
    "world of warcraft",
    "cs go",
    "antarctica",
    "fifa",
    "amsterdam",
    "usa",
    "tesla",
    "economy",
    "ecology",
    "biology"
);

foreach ($queries as $query) {
    $params = [
        "engine" => "google_scholar",
        "q" => $query,
        "hl" => "en"
    ];

    $client = new GoogleSearch(getenv("API_KEY"));
    $response = $client->get_json($params);

    foreach ($response->organic_results as $result) {
        print_r($result->title);
    }
}
?>
