import sqlite3

__author__ = 'rPAHT'

conn = sqlite3.connect('Market.db')
c = conn.cursor()


def calculate_margin(item_id, market_ID, pilot):
    """
    Ok so first we have to lookup the buy and sell prices of the item at that market
    something to the effect of:
    buy = SELECT MIN(Ask) FROM MarketDB WITH ID = ItemID and StationID = MarketID
    sell = SELECT MAX(bid) FROM MarketDB WITH ID = ItemID and StationID = MarketID
    """
    buyprice = 0
    sellprice = 0


def calc_broker_fee(pilot, station):
    """
    :param pilot: This should be a Pilot object that describes the pilot being used
    this simulation
    :param station: This should be the station object
    :return: this should return a constant that represents the multiplier to attach to the
    market order
    """
    broker_relations_skill_level = pilot.get_skill_level("Broker Relations")
    broker_corp = station.corp
    broker_faction = broker_corp.faction.faction_id
    faction_standing = pilot.standing_lookup(broker_faction)
    corporation_standing = pilot.standing_lookup(broker_corp)

    broker_fee = (.01 - .0005 * broker_relations_skill_level) / (
                 2 ** (.1400 * faction_standing + .06000 * corporation_standing))
    return broker_fee


def calc_tax(pilot):
    tax = .015 * (.1 * pilot.skill_level_query("Accounting"))
    return tax


def faction_lookup(market_id):
    """
    :param market_id:This is the ID of the station we are trying to lookup from the DB
    :return:

    We need something to the effect of SELECT Faction FROM StationTable with StationID = MarketID
    """
    tmp = c.execute("SELECT faction from StationList WHERE station_id=?", market_id)
    if len(tmp) == 1:
        return tmp
    else:
        raise Exception('Station not found from MarketID provided')
