from django.shortcuts import render

# 데이터베이스와 형태가 비슷하게 ９개의 상품 선언
product_db = [
    {
        "id": 1,
        "name": "product1",
        "price": 1000,
        "description": "This is product1",
        "image": "product1.jpg",
        "sale_count": 100,
        "star_rating": 4,
    },
    {
        "id": 2,
        "name": "product2",
        "price": 2000,
        "description": "This is product2",
        "image": "product2.jpg",
        "sale_count": 200,
        "star_rating": 3,
    },
    {
        "id": 3,
        "name": "product3",
        "price": 3000,
        "description": "This is product3",
        "image": "product3.jpg",
        "sale_count": 300,
        "star_rating": 5,
    },
    {
        "id": 4,
        "name": "product4",
        "price": 4000,
        "description": "This is product4",
        "image": "product4.jpg",
        "sale_count": 400,
        "star_rating": 4,
    },
    {
        "id": 5,
        "name": "product5",
        "price": 5000,
        "description": "This is product5",
        "image": "product5.jpg",
        "sale_count": 500,
        "star_rating": 3,
    },
    {
        "id": 6,
        "name": "product6",
        "price": 6000,
        "description": "This is product6",
        "image": "product6.jpg",
        "sale_count": 600,
        "star_rating": 5,
    },
    {
        "id": 7,
        "name": "product7",
        "price": 7000,
        "description": "This is product7",
        "image": "product7.jpg",
        "sale_count": 700,
        "star_rating": 4,
    },
    {
        "id": 8,
        "name": "product8",
        "price": 8000,
        "description": "This is product8",
        "image": "product8.jpg",
        "sale_count": 800,
        "star_rating": 3,
    },
    {
        "id": 9,
        "name": "product9",
        "price": 9000,
        "description": "This is product9",
        "image": "product9.jpg",
        "sale_count": 900,
        "star_rating": 5,
    },
]


def index(request):
    # 판매가 가장 많은 상품 6개를 소개해야 한다. 기본은 오름차순 이므로 reverse
    sorted_product = sorted(product_db, key=lambda x: x["sale_count"], reverse=True)[:6]
    # 특정 상품의 star_rating 값이 4라면, [0, 1, 2, 3]이라는 리스트 생성
    # star_rating의 값을 위처럼 변경
    for product in sorted_product:
        product["star_rating"] = list(range(product["star_rating"]))

    context = {"product_db": sorted_product}
    return render(request, "main/index.html", context)


def about(request):
    return render(request, "main/about.html")
