css = """
/* Scraped Replica Test Card Styles */
.test-card {
    background: white;
    border: 2px solid #1a73e8; /* Blue border to match */
    border-radius: 4px;
    padding: 10px 15px;
    cursor: pointer;
    text-align: center;
    transition: background 0.2s;
    color: #333;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
}
.test-card:hover {
    background: #f8f9fa;
}
.test-card-top {
    font-weight: bold;
    font-size: 1.05rem;
    margin-bottom: 5px;
    color: #1a73e8;
}
.test-card hr {
    border: 0;
    border-top: 1px solid #e0e0e0;
    margin: 8px 0;
}
.test-card-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.85rem;
    color: #555;
}
.test-card-icon {
    color: #1a73e8;
    font-size: 1.3rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border: 2px solid #1a73e8;
    border-radius: 50%;
    line-height: 1;
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + css + "\n")
