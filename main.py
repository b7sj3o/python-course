from uvicorn import run


def main():
    run(app='api:api', reload=True)


if __name__ == "__main__":
    main()
