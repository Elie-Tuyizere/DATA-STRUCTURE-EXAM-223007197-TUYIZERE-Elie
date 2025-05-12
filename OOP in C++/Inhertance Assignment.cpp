#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Base Class
class Room {
protected:  
    int roomNumber;
    string roomType;
    bool isBooked;

public:
    Room(int number = 0, string type = "Generic") {
        roomNumber = number;
        roomType = type;
        isBooked = false;
    }

    virtual void displayInfo() {
        cout << "Room #" << roomNumber << " | Type: " << roomType;
        cout << " | Status: " << (isBooked ? "Booked" : "Available") << endl;
    }

    void bookRoom() {
        isBooked = true;
    }

    void checkoutRoom() {
        isBooked = false;
    }

    bool getStatus() {
        return isBooked;
    }

    int getRoomNumber() {
        return roomNumber;
    }

    string getRoomType() {
        return roomType;
    }
};

// Single Inheritance
class SingleRoom : public Room {
public:
    SingleRoom(int number) : Room(number, "Single") {}
};

// Hierarchical Inheritance
class DoubleRoom : public Room {
public:
    DoubleRoom(int number) : Room(number, "Double") {}
};

class SuiteRoom : public Room {
public:
    SuiteRoom(int number) : Room(number, "Suite") {}
};

// Multilevel Inheritance
class VIPRoom : public SuiteRoom {
public:
    VIPRoom(int number) : SuiteRoom(number) {
        roomType = "VIP Suite";
    }
};

// Multiple Inheritance + Hybrid
class BookingManager : public SingleRoom, public DoubleRoom {
private:
    vector<Room*> rooms;

    struct Booking {
        Room* room;
        string guestName;
        int duration;
    };

    vector<Booking> bookings;

public:
    BookingManager() : SingleRoom(0), DoubleRoom(0) {} // Dummy constructor init

    void addRoom(Room* room) {
        rooms.push_back(room);
    }

    void bookRoom(int roomNumber, string guest, int nights) {
        for (size_t i = 0; i < rooms.size(); ++i) {
            if (rooms[i]->getRoomNumber() == roomNumber && !rooms[i]->getStatus()) {
                rooms[i]->bookRoom();
                Booking b;
                b.room = rooms[i];
                b.guestName = guest;
                b.duration = nights;
                bookings.push_back(b);
                cout << "Room #" << roomNumber << " successfully booked for " << guest;
                cout << " for " << nights << " nights.\n";
                return;   
            }
        }
        cout << "Room #" << roomNumber << " is not available or does not exist.\n";
    }

    void showBookings() {
        for (size_t i = 0; i < bookings.size(); ++i) {
            cout << "Room #" << bookings[i].room->getRoomNumber()
                 << " | Type: " << bookings[i].room->getRoomType()
                 << " | Status: Booked\n";
            cout << "Guest: " << bookings[i].guestName
                 << " | Duration: " << bookings[i].duration << " nights\n\n";
        }
    }

    void showAllRooms() {
        for (size_t i = 0; i < rooms.size(); ++i) {
            rooms[i]->displayInfo();
        }
    }
};

// ---- MAIN FUNCTION ----
int main() {
    BookingManager manager;

    // Create and add rooms
    Room r101(101, "Generic");
    SingleRoom s102(102);
    DoubleRoom d103(103);
    SuiteRoom st201(201);
    VIPRoom vip202(202);

    manager.addRoom(&r101);
    manager.addRoom(&s102);
    manager.addRoom(&d103);
    manager.addRoom(&st201);
    manager.addRoom(&vip202);

    cout << "Available Rooms:\n";
    manager.showAllRooms();

    cout << "\nBooking Test:\n";
    manager.bookRoom(201, "Grace", 3);  // Book Suite
    manager.bookRoom(202, "John", 2);   // Book VIP

    cout << "\n--- Bookings ---\n";
    manager.showBookings();

    return 0;
}
