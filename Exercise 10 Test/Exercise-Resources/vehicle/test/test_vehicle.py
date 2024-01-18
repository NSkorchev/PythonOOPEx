from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(
            40.00,
            130.00
        )

    def test_default_consumpion_class_attribute_iscorrect(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initializing(self):
        self.assertEqual(40.00, self.vehicle.fuel)
        self.assertEqual(40.00, self.vehicle.capacity)
        self.assertEqual(130.00, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        self.vehicle.drive(20)
        self.assertEqual(15, self.vehicle.fuel)

    def test_refuel_more_than_capacity_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_add_fuel(self):
        self.vehicle.fuel = 30
        self.vehicle.refuel(10)
        self.assertEqual(40, self.vehicle.fuel)

    def test_correct__str__method(self):
        self.assertEqual("The vehicle has 130.0 horse power " \
                         "with 40.0 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()
