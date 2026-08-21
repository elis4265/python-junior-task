"""Car maintenance logic.

Each docstring describes the agreed behaviour of that function.
"""

SERVICE_INTERVAL = 5000


def is_service_due(current_mileage, last_service_mileage, interval=SERVICE_INTERVAL):
    """True once the car has been driven `interval` miles or more since its last service."""
    return current_mileage - last_service_mileage > interval


def average_mpg(trips):
    """Average miles per gallon over a list of (miles, gallons) trips.

    Returns 0.0 when there is nothing to measure.
    """
    total_miles = sum(trip[0] for trip in trips)
    total_gallons = sum(trip[1] for trip in trips)
    return total_miles / total_gallons


def tire_wear_percent(tire_miles, rated_miles=50000):
    """Percent of tread life used, from 0 to 100. A worn-out tire reports 100."""
    return round(tire_miles / rated_miles * 100)


def add_service(mileage, description, history=[]):
    """Add a service visit to one car's history and return that history."""
    history.append({"mileage": mileage, "description": description})
    return history


def services_since(history, mileage):
    """Every service in the history recorded at or after the given mileage."""
    return [service for service in history if service["mileage"] > mileage]


def forget_services_before(history, mileage):
    """Remove every service recorded before the given mileage. Returns the history."""
    for service in history:
        if service["mileage"] < mileage:
            history.remove(service)
    return history


def split_service_cost(cost, owners):
    """One owner's share of a service bill, in euros and cents, split evenly."""
    return cost // owners
