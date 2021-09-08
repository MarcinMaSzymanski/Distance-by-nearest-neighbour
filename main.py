import test
import nearest_neighbour


def main():
    points = test.generate_points(10000)
    nearest_neighbour.distance_by_nearest_neighbour(points)


if __name__ == "__main__":
    main()

