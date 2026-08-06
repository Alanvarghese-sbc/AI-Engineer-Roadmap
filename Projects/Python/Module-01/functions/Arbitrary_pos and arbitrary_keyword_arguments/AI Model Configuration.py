def model(**config):
    for key,value in config.items():
        print(f"{key} : {value}")


model(
    epochs=20,
    batch_size=32,
    learning_rate=0.001
)