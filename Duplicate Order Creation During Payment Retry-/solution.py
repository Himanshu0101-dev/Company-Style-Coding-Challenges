import java.util.*;

public class DuplicateOrderDetector {

    static class Order {
        String userId;
        int amount;
        int timestamp;

        Order(String userId, int amount, int timestamp) {
            this.userId = userId;
            this.amount = amount;
            this.timestamp = timestamp;
        }
    }

    public static List<String> findDuplicateOrders(List<Order> orders) {
        List<String> result = new ArrayList<>();

        // Key = userId + amount
        Map<String, Integer> lastOrderTime = new HashMap<>();

        for (Order order : orders) {
            String key = order.userId + "_" + order.amount;

            if (lastOrderTime.containsKey(key)) {
                int prevTime = lastOrderTime.get(key);

                if (order.timestamp - prevTime <= 30) {
                    result.add("(" + order.userId + ", "
                            + prevTime + ", "
                            + order.timestamp + ")");
                }
            }

            lastOrderTime.put(key, order.timestamp);
        }

        return result;
    }

    public static void main(String[] args) {

        List<Order> orders = Arrays.asList(
                new Order("U1", 500, 100),
                new Order("U1", 500, 105),
                new Order("U2", 800, 200),
                new Order("U3", 300, 250),
                new Order("U3", 300, 260)
        );

        List<String> duplicates = findDuplicateOrders(orders);

        System.out.println(duplicates);
    }
}
