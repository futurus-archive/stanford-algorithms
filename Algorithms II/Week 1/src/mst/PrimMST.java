// deprecated

package mst;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Comparator;

/**
 * Created by vunguyen on 1/16/17.
 */

class MyComparator implements Comparator<Vertex> {
    @Override
    public int compare(Vertex v1, Vertex v2) {
        return v1.getWeight() - v2.getWeight();
    }
}

class Vertex {
    private int id;
    private int weight;
    public PriorityQueue<Vertex> edges;

    public Vertex(int vid, int w) {
        id = vid;
        weight = w;
        MyComparator comparator = new MyComparator();
        edges = new PriorityQueue<Vertex>(500, comparator);
    }

    public Vertex(Vertex another) {
        id = another.id;
        weight = another.weight;
        edges = another.edges;
    }

    public int getId() {
        return id;
    }

    public int getWeight() {
        return weight;
    }

    public int nEdges() {
        return edges.size();
    }

    public void connect(Vertex to) {
        edges.offer(to);
    }
}


class Graph {
    private ArrayList<Vertex> vertices;

    public Graph() {
        vertices = new ArrayList<Vertex>();
    }

    public int nVertices() {
        return vertices.size();
    }

    public boolean containsVertex(int id) {
        for (Vertex vertex : vertices) {
            if (vertex.getId() == id) {
                return true;
            }
        }

        return false;
    }

    public void addVertex(Vertex v) {
        vertices.add(v);
    }

    public Vertex getVertex(int id) {
        for (Vertex vertex : vertices) {
            if (vertex.getId() == id) {
                return vertex;
            }
        }

        return null;
    }

    public ArrayList<Vertex> getVertices() {
        return vertices;
    }

    public Vertex popVertex(int id) {
        Vertex o = null;
        for (Vertex v : vertices) {
            if (v.getId() == id) {
                o = new Vertex(v);
                vertices.remove(v);
                break;
            }
        }
        return o;
    }
}

public class PrimMST {
    public static Graph getGraph(String filename) throws IOException {
        File file = new File(filename);
        Scanner sc = null;
        Graph g = null;

        try {
            sc = new Scanner(file);
            int nNodes = sc.nextInt();
            int nEdges = sc.nextInt();
            g = new Graph();

            for (int i = 0; i < nEdges; i++) {
                int f = sc.nextInt();
                int t = sc.nextInt();
                int w = sc.nextInt();
                Vertex fV = new Vertex(f, w);
                Vertex fT = new Vertex(t, w);

                if (!g.containsVertex(f)) {
                    g.addVertex(fV);
                }
                g.getVertex(f).connect(fT);

                if (!g.containsVertex(t)) {
                    g.addVertex(fT);
                }
                g.getVertex(t).connect(fV);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (sc != null) {
                sc.close();
            }
            return g;
        }
    }

    public static void main(String[] args) {
        try {
            Graph g = getGraph("data/uedges.txt");
            int size = g.nVertices();
//            for (Vertex vp : g.getVertices()) {
//                System.out.println(vp.getId() + " " + vp.nEdges() + " " + vp.edges.peek().getId());
//                while (vp.edges.size() > 0 && g.containsVertex(vp.edges.peek().getId())) {
//                    System.out.println(vp.getId() + " ---> " + vp.edges.peek().getId() + " w/ " + vp.edges.peek().getWeight());
//                    vp.edges.poll();
//                }
//            }

            Graph t = new Graph();
            long sum = 0;

            Vertex v = g.popVertex(1);
            t.addVertex(v);

            while (t.nVertices() < size) {
                Vertex w;

                if (v.edges.size() > 0) {
                    System.out.println("---------");
                    System.out.println("v: " + v.getId());

                    w = g.popVertex(v.edges.poll().getId());
                    System.out.println("w: " + w.getId() + " --- " + w.getWeight());
                    t.addVertex(w);
                    sum += w.getWeight();

                    int minLen = 1000000;
                    for (Vertex vp : t.getVertices()) {
                        while (vp.edges.size() > 0 && t.containsVertex(vp.edges.peek().getId())) {
                            vp.edges.poll();
                        }

                        if (vp.edges.size() > 0 && vp.edges.peek().getWeight() <= minLen) {
                            System.out.println(vp.getId() + " ---> " + vp.edges.peek().getId() + " w/ " + vp.edges.peek().getWeight() + " and is connected to " + vp.edges.peek().edges.size());
                            v = new Vertex(vp);
                            minLen = vp.edges.peek().getWeight();
                        }
                    }
                }
            }

            System.out.println(sum);
        } catch (IOException e) {
        }
    }
}
