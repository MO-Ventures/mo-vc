import sentry_sdk
sentry_sdk.init(
    "https://4c5f291b7e3d4c7ba44594f42a467a50@o945190.ingest.sentry.io/5893779",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)