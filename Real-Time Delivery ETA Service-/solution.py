from datetime import datetime


class Order:
    def __init__(self, order_id, total_distance):
        self.order_id = order_id
        self.total_distance = total_distance
        self.current_distance = total_distance
        self.created_at = datetime.now()


class Driver:
    def __init__(self, driver_id):
        self.driver_id = driver_id
        self.distance_to_customer = 0


class ETAEngine:
    AVG_SPEED = 30  # km/hr

    @staticmethod
    def calculate_eta(distance):
        eta_hours = distance / ETAEngine.AVG_SPEED
        eta_minutes = eta_hours * 60
        return round(eta_minutes)


class NotificationService:

    @staticmethod
    def send_alert(order_id, message):
        print(f"[ALERT] Order {order_id}: {message}")


class DriverTracker:

    def update_location(self, driver, distance):
        driver.distance_to_customer = distance


class OrderManager:

    DELAY_THRESHOLD = 2

    def __init__(self):
        self.orders = {}
        self.drivers = {}
        self.last_eta = {}

        self.tracker = DriverTracker()
        self.notifier = NotificationService()

    def add_order(self, order, driver):

        self.orders[order.order_id] = order
        self.drivers[order.order_id] = driver

        eta = ETAEngine.calculate_eta(
            driver.distance_to_customer
        )

        self.last_eta[order.order_id] = eta

        print(
            f"Order {order.order_id} created "
            f"ETA = {eta} min"
        )

    def update_driver_location(
            self,
            order_id,
            new_distance
    ):

        driver = self.drivers[order_id]

        self.tracker.update_location(
            driver,
            new_distance
        )

        new_eta = ETAEngine.calculate_eta(
            new_distance
        )

        old_eta = self.last_eta[order_id]

        print(
            f"Order {order_id} -> "
            f"Distance {new_distance} km "
            f"ETA {new_eta} min"
        )

        if new_eta - old_eta >= self.DELAY_THRESHOLD:

            self.notifier.send_alert(
                order_id,
                f"Delivery delayed. "
                f"ETA increased "
                f"from {old_eta} to {new_eta}"
            )

        self.last_eta[order_id] = new_eta


# ----------------
# Driver Code
# ----------------

manager = OrderManager()

order = Order(
    order_id=101,
    total_distance=10
)

driver = Driver(
    driver_id="D1001"
)

driver.distance_to_customer = 2

manager.add_order(
    order,
    driver
)

updates = [1.5, 1.0, 1.2, 3.5]

for distance in updates:
    manager.update_driver_location(
        101,
        distance
    )
