from app.tests.test_database import client


def test_save():
    response = client.post("/api/v1/save-statistics", params={
        "stat_date": "2022-10-20",
        "views": 0,
        "clicks": 0,
        "cost": 0
    })
    assert response.status_code == 200, response.text
    data = response.json()
    assert data['data']['stat_date'] == "2022-10-20"
    assert data['data']['views'] == 0
    assert data['data']['clicks'] == 0
    assert data['data']['cost'] == 0


def test_get():
    save_stat = client.post("/api/v1/save-statistics", params={
        "stat_date": "2022-10-20",
        "views": 0,
        "clicks": 0,
        "cost": 0
    })
    response = client.get("/api/v1/get-statistics", params={'starts': "2022-10-20", 'ends': '2022-10-20'})
    assert response.status_code == 200, response.text
    data = response.json()
    for statistic in data['data']:
        assert statistic['stat_date'] == "2022-10-20"
        assert statistic['views'] == 0
        assert statistic['clicks'] == 0
        assert statistic['cost'] == 0


